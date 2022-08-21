from django.db import models

class CargoManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )

class Cargo(models.Model):

    nome = models.CharField(max_length=50)
    salario = models.FloatField()
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ['nome']
