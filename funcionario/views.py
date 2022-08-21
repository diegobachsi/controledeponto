import string
from django.shortcuts import render
from funcionario.models import Funcionario, SenhaProvisoria

from funcionario.forms import FormPrimeiroAcesso
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def primeiro_acesso(request):

    template = 'primeiro_acesso.html'

    context = {}

    if request.method == "POST":
        form = FormPrimeiroAcesso(request.POST)

        #verifica se o preenchimento do form foi válido
        if form.is_valid():
            context['is_valid'] = True
        
            #recebe os valores digitamos correspondente a cada campo do form
            senha = request.POST['senha']
            repetir_senha = request.POST['repetir_senha']
            matricula = request.POST['matricula']

            primeiro_nome = Funcionario.objects.filter(matricula=matricula).values('primeiro_nome')
            ultimo_nome = Funcionario.objects.filter(matricula=matricula).values('ultimo_nome')

            senha_provisoria = SenhaProvisoria.objects.get(matricula=matricula)
            if not senha_provisoria.is_active:
                messages.error(request,'Usuário já possui senha cadastrada!')
            else:
                if senha == repetir_senha:
                    if validar_senha(senha) == 1:
                        messages.error(request,'A senha precisa ter no mínimo 8 dígitos!')
                    elif validar_senha(senha) == 2:
                        messages.error(request,'A senha precisa ter no mínimo 3 letras!')
                    elif validar_senha(senha) == 3:
                        messages.error(request,'A senha precisa ter no mínimo 3 números!')
                    else:
                        #criptografa senha
                        senha = make_password(password=senha, salt=None, hasher='pbkdf2_sha256')

                        try:
                            usuario = User.objects.get(username=matricula)
                            usuario.set_password(senha)
                            messages.success(request,'Senha alterada com sucesso!')
   
                        except:
                            #salva usuario no model User
                            cadastrar_usuario = User(username=matricula, password=senha, first_name=primeiro_nome, last_name=ultimo_nome)
                            cadastrar_usuario.save()
                            messages.success(request,'Senha cadastrada com sucesso!')

                        #atualiza is_active de senha provisória para False
                        status_senha_provisoria = SenhaProvisoria.objects.filter(matricula=matricula)
                        status_senha_provisoria.update(is_active=False)

                        
                        context['sucess'] = True
                else:
                    messages.error(request,'Senhas estão diferentes!')
                    context['sucess'] = False
                
    else:
        form = FormPrimeiroAcesso()

    context['form'] = form

    return render(request, template, context)

def validar_senha(senha):
    
    lista_senha = list(senha)
    letras = list(string.ascii_lowercase)
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count_letra = 0
    count_num = 0

    if len(senha) < 8:
        return 1
    else:
        for i in lista_senha:
            if i in letras:
                count_letra += 1
            if i in numeros:
                count_num += 1

        if count_letra < 3:
            return 2
        elif count_num < 3:
            return 3
        else:
            return 4

