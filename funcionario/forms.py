from django import forms

class FormPrimeiroAcesso(forms.Form):

    matricula = forms.CharField(label='Matricula', widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Matrícula'}))
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Senha'}))
    repetir_senha = forms.CharField(label='Repetir Senha', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Repetir Senha'}))