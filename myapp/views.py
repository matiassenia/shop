
from django.shortcuts import render, redirect
from .models import Remera
from .forms import RemeraForm

def home ( request ):
    remeras = Remera.objects.all()
    return render(request, "my-app/home.html", {'remeras':remeras})

def add_remera(request):
    if request.method == 'POST':
        form = RemeraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RemeraForm()
    return render (request, 'my-app/add_remera.html', {'form':form})        

def contacto(request):
    return render (request, "my-app/contacto.html")

def base(request):
    return render (request, "my-app/base.html")