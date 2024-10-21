from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Cliente, Producto, Pedido, Blog, Mensaje
from .forms import ClienteForm, ProductoForm, PedidoForm, BuscarClienteForm, BlogForm, MensajeForm

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


def about_view(request):
    return render(request, 'about.html')

def blog_list_view(request):
    blogs = Blog.objects.all()
    if not blogs:
        return render(request, 'pages/blog_list.html', {'mensaje': "No hay páginas aún"})
    return render(request, 'pages/blog_list.html', {'blogs': blogs})

def blog_detail_view(request, pageId):
    blog = get_object_or_404(Blog, id=pageId)
    return render(request, 'pages/blog_detail.html', {'blog': blog})

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def mensaje_view(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajes')
    else:
        form = MensajeForm()
    return render(request, 'messages/mensajes.html', {'form': form})

@login_required
def mensajes_list_view(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'messages/mensajes_list.html', {'mensajes': mensajes})
