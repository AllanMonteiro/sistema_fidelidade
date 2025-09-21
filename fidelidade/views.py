from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from .models import Cliente, Recompensa, Compra
from .forms import ClienteForm, RecompensaForm, CompraForm


def home(request):
    total_clientes = Cliente.objects.count()
    total_compras = Compra.objects.count()
    total_pontos = Cliente.objects.aggregate(total=models.Sum("pontos"))["total"] or 0

    ultimos_clientes = Cliente.objects.order_by("-id")[:5]
    ultimas_compras = Compra.objects.order_by("-data")[:5]

    context = {
        "total_clientes": total_clientes,
        "total_compras": total_compras,
        "total_pontos": total_pontos,
        "ultimos_clientes": ultimos_clientes,
        "ultimas_compras": ultimas_compras,
    }
    return render(request, "fidelidade/home.html", context)


# ===============================
# CLIENTES
# ===============================
def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, "fidelidade/clientes_list.html", {"clientes": clientes})


def clientes_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fidelidade:clientes_list")
    else:
        form = ClienteForm()
    return render(request, "fidelidade/clientes_form.html", {"form": form})


def clientes_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("fidelidade:clientes_list")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "fidelidade/clientes_form.html", {"form": form})


def clientes_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect("fidelidade:clientes_list")
    return render(request, "fidelidade/cliente_confirm_delete.html", {"object": cliente})


# ===============================
# RECOMPENSAS
# ===============================
def recompensas_list(request):
    recompensas = Recompensa.objects.all()
    return render(request, "fidelidade/recompensas_list.html", {"recompensas": recompensas})


def recompensas_create(request):
    if request.method == "POST":
        form = RecompensaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fidelidade:recompensas_list")
    else:
        form = RecompensaForm()
    return render(request, "fidelidade/recompensas_form.html", {"form": form})


def recompensas_update(request, pk):
    recompensa = get_object_or_404(Recompensa, pk=pk)
    if request.method == "POST":
        form = RecompensaForm(request.POST, instance=recompensa)
        if form.is_valid():
            form.save()
            return redirect("fidelidade:recompensas_list")
    else:
        form = RecompensaForm(instance=recompensa)
    return render(request, "fidelidade/recompensas_form.html", {"form": form})


def recompensas_delete(request, pk):
    recompensa = get_object_or_404(Recompensa, pk=pk)
    if request.method == "POST":
        recompensa.delete()
        return redirect("fidelidade:recompensas_list")
    return render(request, "fidelidade/recompensa_confirm_delete.html", {"object": recompensa})


# ===============================
# COMPRAS
# ===============================
def compras_list(request):
    compras = Compra.objects.all()
    return render(request, "fidelidade/compras_list.html", {"compras": compras})


def compras_create(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fidelidade:compras_list")
    else:
        form = CompraForm()
    return render(request, "fidelidade/compras_form.html", {"form": form})


def compras_update(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == "POST":
        form = CompraForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            return redirect("fidelidade:compras_list")
    else:
        form = CompraForm(instance=compra)
    return render(request, "fidelidade/compras_form.html", {"form": form})


def compras_delete(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == "POST":
        compra.delete()
        return redirect("fidelidade:compras_list")
    return render(request, "fidelidade/compra_confirm_delete.html", {"object": compra})
