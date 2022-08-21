from django.contrib import admin

from .models import Ponto

class PontoAdmin(admin.ModelAdmin):

    list_display = ['matricula', 'hora', 'data', 'tipo', 'validacao_provisoria', 'validacao_definitiva']
    search_fields = ['matricula']

admin.site.register(Ponto, PontoAdmin)
