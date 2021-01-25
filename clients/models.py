from django.db import models
from datetime import datetime


# Create your models here.

class Client(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=13)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome