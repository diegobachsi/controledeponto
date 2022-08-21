from django import views
from django.urls import path

from . import views

app_name = 'supervisor'

urlpatterns = [
    path('form_resetar_senha/', views.form_resetar_senha, name='form_resetar_senha'),
    path('resetar_senha/', views.resetar_senha, name='resetar_senha'),
    path('form_validar_ponto/', views.form_validar_ponto, name='form_validar_ponto'),
    path('validar_ponto/', views.validar_ponto, name='validar_ponto'),
    path('validar_ponto_sucess/', views.validar_ponto_sucess, name='validar_ponto_sucess'),
]