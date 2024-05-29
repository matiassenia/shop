
from django.urls import path
from . import views

urlpatterns = [
      path( '' , views.home, name = "home" ),
      path( 'contacto' , views.contacto, name = "contacto"),
      path( 'base' , views.base, name = "base"),
      path( 'nueva-remera' , views.add_remera, name = 'add_remera'),
      
]
