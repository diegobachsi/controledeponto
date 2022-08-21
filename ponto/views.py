from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cargo.models import Cargo
from funcionario.models import Funcionario
from setor.models import Setor

from .models import Ponto

@login_required(login_url='autenticacao:login')
def index(request):

    #inicia o contexto
    context = {}

    #registra o template responsável
    template = 'ponto.html'

    #data e hora atual
    dt = datetime.now()
    data = dt.strftime("%d/%m/%Y")
    hora = dt.strftime("%H:%M:%S")

    #recuperar dados funci
    context = recuperar_dados_funci(request, data, hora)

    #converte a entrada para datetime para gravar no banco
    data = data_string_to_datetime(data)
    hora = hora_string_to_datetime(hora)

    #verifica se existe registro de ponto
    if verificar_ponto(request.user, data) != None:

        #guarda os contextos de ponto
        context['dados_ponto'] = recuperar_dados_ponto(request.user, data)

        #se verificar_ponto retorna True é porque só existe ENTRADA
        if verificar_ponto(request.user, data):

            #logo o btn_registrar deve aparecer SAIR
            context['btn_registrar'] = 'SAIR'
        else:

            #senão verificar_ponto retornou False, já teve saída, portanto ponto_encerrado.
            context['ponto_encerrado'] = True
    else:
        #senão ainda não teve registro de ponto btn_registrar deve aparecer ENTRAR
        context['btn_registrar'] = 'ENTRAR'


    return render(request, template, context)

@login_required(login_url='autenticacao:login')
def registrar(request):

    context = {}
    template = 'ponto.html'

    #data e hora atual
    dt = datetime.now()
    data_atual_str = dt.strftime("%d/%m/%Y")
    hora_atual_str = dt.strftime("%H:%M:%S")

    #calcular saida
    saida = calcular_saida(request, data_atual_str, hora_atual_str)

    #converte a saida para string separado
    data_saida_str = saida.strftime("%d/%m/%Y")
    hora_saida_str = saida.strftime("%H:%M:%S")

    #converte a entrada para datetime para gravar no banco
    data_atual_dtime = data_string_to_datetime(data_atual_str)
    hora_atual_dtime = hora_string_to_datetime(hora_atual_str)

    if verificar_ponto(request.user, data_atual_dtime) == None:

        #gravar a entrada no ponto
        ponto = Ponto(matricula=request.user, data=data_atual_dtime, hora=hora_atual_dtime, tipo='ENTRADA')
        ponto.save()
           
        #recuperar dados funci
        context = recuperar_dados_funci(request, data_atual_str, hora_atual_str)

        #registra o contexto que o ponto foi registrado
        context['registro_sucess'] = True

        #guarda os contextos de ponto
        context['dados_ponto'] = recuperar_dados_ponto(request.user, data_atual_dtime)

    elif verificar_ponto(request.user, data_atual_dtime):

        #gravar a entrada no ponto
        ponto = Ponto(matricula=request.user, data=data_atual_dtime, hora=hora_atual_dtime, tipo='SAIDA')
        ponto.save()

        #recuperar dados funci
        context = recuperar_dados_funci(request, data_atual_str, hora_atual_str)

        #registra o contexto que o ponto foi registrado
        context['registro_sucess'] = True

        #guarda os contextos de ponto
        context['dados_ponto'] = recuperar_dados_ponto(request.user, data_atual_dtime)

    else:
        pass

    #guarda os contextos de saida
    context['data_saida'] = data_saida_str
    context['hora_saida'] = hora_saida_str

    return render(request, template, context)

@login_required(login_url='autenticacao:login')
def consultar_ponto(request):

    #inicia o contexto
    context = {}

    #registra o template responsável
    template = 'consultar_ponto.html'

    #data e hora atual
    dt = datetime.now()
    data_atual_str = dt.strftime("%d/%m/%Y")
    hora_atual_str = dt.strftime("%H:%M:%S")

    #recuperar dados funci
    context = recuperar_dados_funci(request, data_atual_str, hora_atual_str)

    #converte a entrada para datetime para gravar no banco
    data_atual_dtime = data_string_to_datetime(data_atual_str)

    #guarda o context
    context['ponto'] = recuperar_dados_ponto(request.user, data_atual_dtime)

    print(context['ponto'])

    return render(request, template, context)

@login_required(login_url='autenticacao:login')
def confirmar_validacao_ponto(request):

    context = {}

    #registra o template responsável
    template = 'confirmar_validacao_ponto.html'

    pontos = Ponto.objects.filter(matricula=request.user, validacao_provisoria=True, validacao_definitiva=False)

    id = request.GET.get('idponto')

    if id != None:
        #recupera o ponto via matricula e id para encontrar a data que deverá ser validada
        ponto = Ponto.objects.filter(id=id).values('data')

        #filtra o ponto por matricula e data para validar
        ponto = Ponto.objects.filter(matricula=request.user, data=ponto[0]['data'])
        ponto.update(validacao_definitiva=True)

        #contexto para indicar que a validação foi realizada com sucesso
        context['validar_ponto_sucess'] = True

    #guarda os pontos a validar
    context['pontos'] = pontos

    return render(request, template, context)

def calcular_saida(request, data_entrada, hora_entrada):

    #recuperar a carga horária
    funci = Funcionario.objects.get(matricula=request.user)
    cargo = Cargo.objects.get(nome=funci.id_cargo)

    date_time_obj = datetime.strptime(data_entrada + ' ' + hora_entrada, '%d/%m/%Y %H:%M:%S')

    hora_saida = timedelta(days=0, hours=cargo.carga_horaria, minutes=0, seconds=0)

    return date_time_obj + hora_saida

def recuperar_dados_ponto(usuario, data):

    ponto = Ponto.objects.filter(matricula=usuario, data=data).values('tipo', 'data', 'hora')

    return ponto

def data_string_to_datetime(data):

    data = datetime.strptime(data, '%d/%m/%Y')

    return data
    
def hora_string_to_datetime(hora):

    hora = datetime.strptime(hora, '%H:%M:%S')

    return hora

def verificar_ponto(usuario, data):

    #recupera os dados do ponto por matricula e data
    ponto = Ponto.objects.filter(matricula=usuario, data=data).values('tipo')

    #se existir dados de ponto verifica qual tipo, senão retorna None
    if ponto:
        try:
            # tenta verifica se existe ponto[1] que é registro para SAIDA
            if ponto[1]:
                return False
        except:
            #se não existe o ponto[1] dará uma exceção e logo só existirá o ponto[0] que é a ENTRADA
            return True
    else:
        return None

def recuperar_dados_funci(request, data, hora):

    context = {}

    #contextos para data, hora e usuario
    funci = Funcionario.objects.get(matricula=request.user)
    setor = Setor.objects.get(nome=funci.id_setor)
    cargo = Cargo.objects.get(nome=funci.id_cargo)

    context['data'] = data
    context['hora'] = hora
    context['matricula'] = request.user
    context['setor'] = setor
    context['cargo'] = cargo

    return context



