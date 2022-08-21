from datetime import datetime
from django.db import models

class Ponto(models.Model):

    matricula = models.CharField(max_length=10)
    data = models.DateField(default=datetime.now)
    hora = models.TimeField(default=datetime.now)
    tipo = models.CharField(max_length=50)
    validacao_provisoria = models.BooleanField(default=False)
    validacao_definitiva = models.BooleanField(default=False)


    def __str__(self):
        return self.matricula


    
