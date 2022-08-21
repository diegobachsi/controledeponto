from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

from autenticacao.forms import FormLogin
from funcionario.models import Funcionario, SenhaProvisoria

def logar(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        try:
            senha_provisoria = SenhaProvisoria.objects.get(matricula=username)
        except:
            pass
        if usuario is not None and not senha_provisoria.is_active:
            login(request, usuario)
            return redirect('home:index')
        else:
            try:
                user = User.objects.get(username=username)
                if not user.is_active:
                    messages.error(request,'Este usuário não está ativo!')
                elif not user.check_password(password) and not senha_provisoria.is_active:
                    messages.error(request,'Senha incorreta!')
                else:
                    messages.error(request,'Sua senha expirou, informe sua senha provisória!')
                    if controle_de_acesso(request, username, password) != None:
                        context = controle_de_acesso(request, username, password)
                form = FormLogin()
            except:
                if controle_de_acesso(request, username, password) != None:
                    context = controle_de_acesso(request, username, password)

                form = FormLogin()
    else:
        form = FormLogin()

    context['form'] = form

    return render(request,'login.html', context)

def controle_de_acesso(request, username, password):

    context = {}

    try:
        funci = Funcionario.objects.get(matricula=username)
        if funci.is_active:
            try:
                senha_provisoria = SenhaProvisoria.objects.get(matricula=username)
                if senha_provisoria.senha_provisoria == password:
                    context['funci_sem_senha'] = True
                    context['username'] = username

                    return context
                else:
                    messages.error(request,'Senha provisória incorreta!')
            except:
                messages.error(request,'Senha provisória não cadastrada!')
        else:
            messages.error(request,'Este usuário não está ativo!')
    except:
        messages.error(request,'Este usuário não existe!')

    return None