
from django.shortcuts import render


def index ( request ):
    return render(request, "my-app/index.html")

def contacto(request):
    return render (request, "my-app/contacto.html")

def base(request):
    return render (request, "my-app/base.html")