
from django.urls import path
#from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
      path( '' , views.home, name = "home" ),
      path( 'contacto', views.contacto, name = "contacto"),
      path( 'base', views.base, name = "base"),
      path( 'carrito/', views.carrito, name='carrito'),
      path( 'agregar-al-carrito/<int:remera_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
      path( 'eliminar-elemento-carrito/<int:elemento_id>/', views.eliminar_elemento_carrito, name='eliminar_elemento_carrito'),
      path( 'actualizar-cantidad-elemento-carrito/<int:elemento_id>/', views.actualizar_cantidad_elemento_carrito, name='actualizar_cantidad_elemento_carrito'),
      path( 'registro/', views.registro, name='registro'),
      path( 'login/', views.login_view, name='login_view'),

]
