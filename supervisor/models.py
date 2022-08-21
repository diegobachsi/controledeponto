from django.db import models
from funcionario.models import Funcionario

from setor.models import Setor

class Supervisor(models.Model):

    funci = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    id_setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Supervisor'
        verbose_name_plural = 'Supervisores'
        ordering = ['id']
