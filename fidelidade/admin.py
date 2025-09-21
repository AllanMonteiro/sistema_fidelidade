from django.contrib import admin
from .models import Cliente, Recompensa


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'bairro', 'pontos')
    search_fields = ('nome', 'telefone', 'bairro')
    list_filter = ('bairro',)
    ordering = ('nome',)
    list_per_page = 20
    readonly_fields = ('id',)


@admin.register(Recompensa)
class RecompensaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'pontos_necessarios')
    search_fields = ('nome',)
    ordering = ('pontos_necessarios',)
    list_per_page = 20
    readonly_fields = ('id',)
