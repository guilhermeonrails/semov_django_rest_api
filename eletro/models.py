from django.db import models

class Eletro(models.Model):
    nome = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    capacidade = models.CharField(max_length=30)
    onde_usamos = models.CharField(max_length=30)
    preco = models.IntegerField()
    ja_teve_conserto = models.BooleanField()