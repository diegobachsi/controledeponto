from django.contrib import admin

from .models import Setor

class SetorAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome']
    search_fields = ['id', 'nome']

admin.site.register(Setor, SetorAdmin)
