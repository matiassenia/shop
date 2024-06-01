
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Remera, Carrito, ElementoCarrito


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


def agregar_al_carrito(request, remera_id):
    remera = get_object_or_404(Remera, id=remera_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user, activo=True)
    elemento_carrito, created = ElementoCarrito.objects.get_or_create(carrito=carrito, remera=remera)
    
    if not created:
        elemento_carrito.cantidad += 1
        elemento_carrito.save()
    
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user, activo=True).first()
    elementos = carrito.elementos.all() if carrito else []
    return render(request, 'shop/carrito.html', {'carrito': carrito, 'elementos': elementos})

@login_required
def eliminar_elemento_carrito(request, elemento_id):
    elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
    elemento.delete()
    return redirect('ver_carrito')

@login_required
def actualizar_cantidad_elemento_carrito(request, elemento_id, nueva_cantidad):
    elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
    elemento.cantidad = nueva_cantidad
    elemento.save()
    return redirect('ver_carrito')