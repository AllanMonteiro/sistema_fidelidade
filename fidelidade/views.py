from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Cliente, Recompensa
from .forms import ClienteForm, RecompensaForm

# Página inicial / Dashboard
def index(request):
    return render(request, "fidelidade/index.html")

# Listar clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "fidelidade/listar_clientes.html", {"clientes": clientes})

# Cadastrar cliente
def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect("clientes_list")
    else:
        form = ClienteForm()
    return render(request, "fidelidade/cadastrar_cliente.html", {"form": form})

# Editar cliente
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente atualizado com sucesso!")
            return redirect("clientes_list")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "fidelidade/editar_cliente.html", {"form": form})

# Apagar cliente
def apagar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    messages.success(request, "Cliente apagado com sucesso!")
    return redirect("clientes_list")

# Adicionar pontos (valor em R$ convertido para pontos)
def adicionar_pontos(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        valor = float(request.POST.get("valor", 0))  # Valor em R$
        pontos_adicionados = valor * 0.1  # 0,1 ponto por 1 real
        cliente.pontos += pontos_adicionados
        cliente.save()
        messages.success(request, f"{pontos_adicionados:.2f} pontos adicionados para {cliente.nome}!")
        return redirect("clientes_list")
    return render(request, "fidelidade/adicionar_pontos.html", {"cliente": cliente})

def resgatar_recompensa(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    recompensas = Recompensa.objects.all()

    if request.method == "POST":
        recompensa_id = request.POST.get("recompensa")
        recompensa = get_object_or_404(Recompensa, id=recompensa_id)
        if cliente.pontos >= recompensa.pontos_necessarios:
            cliente.pontos -= recompensa.pontos_necessarios
            cliente.save()
            messages.success(request, f"Recompensa '{recompensa.nome}' resgatada com sucesso!")
        else:
            messages.error(request, "Pontos insuficientes para resgatar essa recompensa.")
        return redirect("clientes_list")

    return render(request, "fidelidade/resgatar_recompensa.html", {"cliente": cliente, "recompensas": recompensas})
# Cadastrar recompensa
def cadastrar_recompensa(request):
    if request.method == "POST":
        form = RecompensaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Recompensa cadastrada com sucesso!")
            return redirect("index")
    else:
        form = RecompensaForm()
    return render(request, "fidelidade/cadastrar_recompensa.html", {"form": form})
