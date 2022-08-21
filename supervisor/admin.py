from django.contrib import admin

from .models import Supervisor

class SupervisorAdmin(admin.ModelAdmin):

    list_display = ['id', 'funci', 'id_setor']
    search_fields = ['id', 'id_setor']

admin.site.register(Supervisor, SupervisorAdmin)