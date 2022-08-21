from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ponto.models import Ponto
from .models import Supervisor
from funcionario.models import Funcionario, SenhaProvisoria
from django.contrib import messages

@login_required(login_url='autenticacao:login')
def form_resetar_senha(request):

	context = {}
	template = 'resetar_senha.html'

	context = lista_funci_resetar_senha(request)
	
	return render(request, template, context)

@login_required(login_url='autenticacao:login')
def resetar_senha(request):

	context = {}
	template = 'resetar_senha.html'

	try:
		#recuperar POST
		matricula = request.POST['funci']
	except:
		#caso não informe nenhum funcionário 
		matricula = 'except'

	#tratamento para não selecionar o primeiro Option do Select que é apenas msg ao usuário
	if matricula[0] == 'F':

		#pegar o valor da senha provisoria
		senha_provisoria = SenhaProvisoria.objects.get(matricula=matricula[:10])

		#verifica se a senha provisória está ativa
		if not senha_provisoria.is_active:

			#passa o valor da senha via contexto
			context['senha_provisoria'] = senha_provisoria.senha_provisoria

			#alterar o is_active da senha provisória
			senha_provisoria = SenhaProvisoria.objects.filter(matricula=matricula[:10])
			senha_provisoria.update(is_active=True)

			#passa via contexto que a senha foi resetada
			context['resetar_senha_submit'] = True

		else:
			context = lista_funci_resetar_senha(request)
			messages.error(request, f'Senha do {matricula} já foi resetada! Realizar o acesso com senha provisória.')
	elif matricula == 'except':
		context = lista_funci_resetar_senha(request)
		messages.error(request, 'Nenhum funcionário foi selecionado!')
	else:
		context = lista_funci_resetar_senha(request)
		messages.error(request, 'Esse opção não pode ser selecionada!')

	return render(request, template, context)

@login_required(login_url='autenticacao:login')
def form_validar_ponto(request):

	context = {}
	template = 'validar_ponto.html'

	context = lista_funci_validar_ponto(request)
	
	return render(request, template, context)

@login_required(login_url='autenticacao:login')
def validar_ponto(request):

	context = {}
	template = 'validar_ponto.html'

	try:
		#recuperar POST
		matricula = request.POST['funci']
	except:
		#caso não informe nenhum funcionário 
		matricula = 'except'

	#tratamento para não selecionar o primeiro Option do Select que é apenas msg ao usuário
	if matricula[0] == 'F':

		pontos = Ponto.objects.filter(matricula=matricula[:10], validacao_provisoria=False)

		context['pontos'] = pontos

		#passa via contexto que a senha foi resetada
		context['validar_ponto_submit'] = True

	elif matricula == 'except':
		context = lista_funci_resetar_senha(request)
		messages.error(request, 'Nenhum funcionário foi selecionado!')
		
	else:
		context = lista_funci_resetar_senha(request)
		messages.error(request, 'Esse opção não pode ser selecionada!')

	return render(request, template, context)

def validar_ponto_sucess(request):

	context = {}
	template = 'validar_ponto.html'

	matricula = request.GET.get('matricula')
	id = request.GET.get('idponto')

	#recupera o ponto via matricula e id para encontrar a data que deverá ser validada
	ponto = Ponto.objects.filter(id=id).values('data')

	#filtra o ponto por matricula e data para validar
	ponto = Ponto.objects.filter(matricula=matricula, data=ponto[0]['data'])
	ponto.update(validacao_provisoria=True)

	context['validar_ponto_submit'] = True
	context['validar_ponto_sucess'] = True
	
	return render(request, template, context)

def lista_funci_resetar_senha(request):

	context = {}

	try:
		#recupera o funcionário supervisor
		funci_supervisor = Funcionario.objects.get(matricula=request.user)

		#recupera o objeto supervisor
		supervisor = Supervisor.objects.get(funci=funci_supervisor)

		#filtrar matricula e primeiro nome dos funcis por setor do supervisor
		funcis = Funcionario.objects.filter(id_setor=supervisor.id_setor).values('matricula', 'primeiro_nome')

		#lista para armazenar as matriculas e primeiro nome e lançar no contexto options para o Select
		lista_funci = ['Selecione o funcionário']

		#laço para guardar as informações em String
		for i in funcis:
			lista_funci.append('{} - {}'.format(i.get('matricula'), i.get('primeiro_nome')))

		context['options'] = lista_funci
	except:
		context['options'] = None

	return context

def lista_funci_validar_ponto(request):

	context = {}

	try:
		#recupera o funcionário supervisor
		funci_supervisor = Funcionario.objects.get(matricula=request.user)

		#recupera o objeto supervisor
		supervisor = Supervisor.objects.get(funci=funci_supervisor)

		#filtrar matricula e primeiro nome dos funcis por setor do supervisor
		funcis = Funcionario.objects.filter(id_setor=supervisor.id_setor).values('matricula', 'primeiro_nome')

		#lista para armazenar as matriculas e primeiro nome e lançar no contexto options para o Select
		lista_funci = ['Selecione o funcionário']

		#laço para guardar as informações em String
		for funci in funcis:
			lista_funci.append('{} - {}'.format(funci.get('matricula'), funci.get('primeiro_nome')))

		context['options'] = lista_funci
	except:
		context['options'] = None

	return context
