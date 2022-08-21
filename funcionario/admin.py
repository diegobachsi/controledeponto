from django.contrib import admin

from .models import Funcionario, SenhaProvisoria

class FuncionarioAdmin(admin.ModelAdmin):

    list_display = ['matricula', 'primeiro_nome', 'telefone', 'id_setor', 'is_active']
    search_fields = ['matricula', 'cpf']

admin.site.register(Funcionario, FuncionarioAdmin)

class SenhaProvisoriaAdmin(admin.ModelAdmin):

    list_display = ['matricula', 'senha_provisoria', 'is_active']
    search_fields = ['matricula']

admin.site.register(SenhaProvisoria, SenhaProvisoriaAdmin)
