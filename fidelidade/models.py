from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    pontos = models.FloatField(default=0)

    @property
    def valor_reais(self):
        return self.pontos / 0.1  # Cada ponto = 1/0.1 = 10 reais

    def __str__(self):
        return self.nome

class Recompensa(models.Model):
    nome = models.CharField(max_length=100)
    pontos_necessarios = models.FloatField()
    descricao = models.TextField(blank=True)

    @property
    def valor_reais(self):
        return self.pontos_necessarios / 0.1  # Mesma regra

    def __str__(self):
        return self.nome


