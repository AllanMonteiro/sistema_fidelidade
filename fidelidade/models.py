from django.core.exceptions import ValidationError
from decimal import Decimal
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # ✅ evita duplicados
    telefone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    pontos = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nome} - {self.pontos} pontos"


class Recompensa(models.Model):
    nome = models.CharField(max_length=100)
    pontos_necessarios = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.pontos_necessarios} pontos)"


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    pontos_usados = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    recompensa = models.ForeignKey(Recompensa, on_delete=models.SET_NULL, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Validação antes de salvar"""
        if self.pontos_usados > self.cliente.pontos:
            raise ValidationError("O cliente não possui pontos suficientes para este resgate.")

    def save(self, *args, **kwargs):
        self.clean()  # ✅ garante validação antes de salvar

        if not self.pk:  # Só quando é nova compra
            pontos_ganhos = self.valor_compra * Decimal("0.1")

            # Atualiza pontos do cliente
            self.cliente.pontos += pontos_ganhos
            self.cliente.pontos -= self.pontos_usados
            self.cliente.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Compra de {self.cliente.nome} em {self.data.strftime('%d/%m/%Y')}"

