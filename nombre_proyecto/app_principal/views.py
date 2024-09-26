from django.shortcuts import render, get_object_or_404
from .models import Cliente, Producto, Pedido
from .forms import ClienteForm, ProductoForm, PedidoForm, BuscarClienteForm

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'crear_cliente.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PedidoForm()
    return render(request, 'crear_pedido.html', {'form': form})

def buscar_cliente(request):
    form = BuscarClienteForm()
    clientes = []
    if request.method == 'GET':
        form = BuscarClienteForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            correo = form.cleaned_data.get('correo')
            if nombre:
                clientes = Cliente.objects.filter(nombre__icontains=nombre)
            if correo:
                clientes = Cliente.objects.filter(correo__icontains=correo)
    return render(request, 'buscar_cliente.html', {'form': form, 'clientes': clientes})
