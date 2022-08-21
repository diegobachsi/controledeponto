from django.contrib import admin

from .models import Cargo

class CargoAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome', 'carga_horaria']
    search_fields = ['id', 'nome']

admin.site.register(Cargo, CargoAdmin)
