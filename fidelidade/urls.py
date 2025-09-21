from django.urls import path
from . import views

app_name = "fidelidade"  # ✅ necessário para usar {% url 'fidelidade:...' %}

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # ===============================
    # CLIENTES
    # ===============================
    path("clientes/", views.clientes_list, name="clientes_list"),
    path("clientes/novo/", views.clientes_create, name="clientes_create"),
    path("clientes/<int:pk>/editar/", views.clientes_update, name="clientes_update"),
    path("clientes/<int:pk>/excluir/", views.clientes_delete, name="clientes_delete"),

    # ===============================
    # RECOMPENSAS
    # ===============================
    path("recompensas/", views.recompensas_list, name="recompensas_list"),
    path("recompensas/nova/", views.recompensas_create, name="recompensas_create"),
    path("recompensas/<int:pk>/editar/", views.recompensas_update, name="recompensas_update"),
    path("recompensas/<int:pk>/excluir/", views.recompensas_delete, name="recompensas_delete"),

    # ===============================
    # COMPRAS
    # ===============================
    path("compras/", views.compras_list, name="compras_list"),
    path("compras/nova/", views.compras_create, name="compras_create"),
    path("compras/<int:pk>/editar/", views.compras_update, name="compras_update"),
    path("compras/<int:pk>/excluir/", views.compras_delete, name="compras_delete"),
]
