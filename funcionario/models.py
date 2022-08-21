from django.db import models

from cargo.models import Cargo
from setor.models import Setor

class FuncionarioManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )

class Funcionario(models.Model):

    matricula = models.CharField(max_length=10, primary_key=True)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.DO_NOTHING)
    id_setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)
    primeiro_nome = models.CharField(max_length=255)
    ultimo_nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=40, blank=True)
    email = models.CharField(max_length=40, blank=True)
    endereco = models.CharField(max_length=100)
    dt_nascimento = models.DateField()
    dt_admissao = models.DateField(auto_now_add=True)
    dt_demissao = models.DateField(blank=True, null=True)
    is_active = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.primeiro_nome

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering = ['matricula']

class SenhaProvisoria(models.Model):

    matricula = models.CharField(max_length=10)
    senha_provisoria = models.CharField(max_length=50)
    is_active = models.BooleanField('Ativa', default=True)
