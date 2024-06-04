
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Remera, Carrito, ElementoCarrito
from .forms import RegistroForm

#
@login_required
def home ( request ):
    remeras = Remera.objects.all()
    return render(request, "shop/home.html", {'remeras':remeras})

@login_required
def contacto(request):
    return render (request, "shop/contacto.html")

@login_required
def base(request):
    return render (request, "shop/base.html")

@login_required
def agregar_al_carrito(request, remera_id):
    remera = get_object_or_404(Remera, id=remera_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user, activo=True)
    elemento_carrito, created = ElementoCarrito.objects.get_or_create(carrito=carrito, remera=remera)
    
    if not created:
        elemento_carrito.cantidad += 1
        elemento_carrito.save()
    
    return redirect('carrito')

#Vista del estado del carrito
@login_required
def carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user, activo=True).first()
    elementos = carrito.elementos.all() if carrito else []
    total_compra = sum(elemento.get_total_precio() for elemento in elementos)
    return render(request, 'shop/carrito.html', {'carrito': carrito, 'elementos': elementos, 'total_compra':total_compra})

@login_required
def eliminar_elemento_carrito(request, elemento_id):
    elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
    elemento.delete()
    return redirect('carrito')

@login_required
def actualizar_cantidad_elemento_carrito(request, elemento_id):
    if request.method == "POST":
        nueva_cantidad = request.POST.get('cantidad')
        if nueva_cantidad is not None:
            try: 
                nueva_cantidad=int(nueva_cantidad)      
                elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
                elemento.cantidad = nueva_cantidad
                elemento.save()
            except ValueError:
                pass
    return redirect('carrito')


#Registro de usuario

def registro(request):
    if request.method == 'POST':
        form = RegistroForm (request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Registro exitoso! Bienvenido {user.username}!')
            return redirect('base')
    else:
        form = RegistroForm()
        messages.error(request, 'Hubo un error intenta nuevamente.')
    return render(request, 'registration/registro.html', {'form': form})    


#Login y autenticación
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #Autenticación del usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si el usuario es autenticado correctamente, inicia sesión
            login(request, user)
            messages.success(request, f'Bienvenido de nuevo{user.username}!')
        else:
            # Si el usuario no puede ser autenticado, muestra un mensaje de error
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'login.html')