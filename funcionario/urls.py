from django import views
from django.urls import path

from . import views

app_name = 'funcionario'

urlpatterns = [
    path('primeiro_acesso/', views.primeiro_acesso, name='primeiro_acesso'),
]