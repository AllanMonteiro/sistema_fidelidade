from django import forms
from .models import Cliente, Recompensa

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "telefone", "bairro"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "telefone": forms.TextInput(attrs={"class": "form-control"}),
            "bairro": forms.TextInput(attrs={"class": "form-control"}),
        }

class RecompensaForm(forms.ModelForm):
    class Meta:
        model = Recompensa
        fields = ["nome", "pontos_necessarios", "descricao"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "pontos_necessarios": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
