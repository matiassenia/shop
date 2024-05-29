
from django.urls import path
from . import views

urlpatterns = [
      path( "" , views.index, name = "index" ),
      path( "contacto", views.contacto, name= "contacto"),
      path( "base", views.base, name= "base")
]
