from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.listar_clientes, name='clientes_list'),
    path('clientes/novo/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:cliente_id>/adicionar_pontos/', views.adicionar_pontos, name='adicionar_pontos'),
    path('clientes/<int:cliente_id>/resgatar/', views.resgatar_recompensa, name='resgatar_recompensa'),
    path('clientes/<int:cliente_id>/apagar/', views.apagar_cliente, name='apagar_cliente'),
    path('recompensas/novo/', views.cadastrar_recompensa, name='cadastrar_recompensa'),
]
