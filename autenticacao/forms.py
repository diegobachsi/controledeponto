from django import forms
from django.contrib.auth.forms import AuthenticationForm

class FormLogin(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Matrícula'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Senha'})
    )