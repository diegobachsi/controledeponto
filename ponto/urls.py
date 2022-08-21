from django import views
from django.urls import path

from . import views

app_name = 'ponto'

urlpatterns = [
    path('ponto/', views.index, name='index'),
    path('registrar_ponto/', views.registrar, name='registrar_ponto'),
    path('consultar_ponto/', views.consultar_ponto, name='consultar_ponto'),
    path('confirmar_validacao_ponto/', views.confirmar_validacao_ponto, name='confirmar_validacao_ponto'),
]