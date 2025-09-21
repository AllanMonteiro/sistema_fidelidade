from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente, Recompensa, Compra
from decimal import Decimal


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "telefone", "bairro"]


class RecompensaForm(forms.ModelForm):
    class Meta:
        model = Recompensa
        fields = ["nome", "pontos_necessarios", "descricao"]


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ["cliente", "valor_compra", "pontos_usados", "recompensa"]

    def clean(self):
        cleaned_data = super().clean()
        cliente = cleaned_data.get("cliente")
        pontos_usados = cleaned_data.get("pontos_usados") or Decimal("0")

        # 🔒 Validação principal
        if cliente and pontos_usados > cliente.pontos:
            raise ValidationError(
                {"pontos_usados": f"O cliente {cliente.nome} não possui pontos suficientes."}
            )

        # 🔒 Se tiver recompensa vinculada, precisa usar ao menos os pontos necessários
        recompensa = cleaned_data.get("recompensa")
        if recompensa and pontos_usados < recompensa.pontos_necessarios:
            raise ValidationError(
                {"pontos_usados": f"A recompensa '{recompensa.nome}' exige {recompensa.pontos_necessarios} pontos."}
            )

        return cleaned_data
