from django.db import models
from django.conf import settings
class Remera(models.Model):
    
    TALLE_CHOICES = [
        (1, 'XS'),
        (2, 'S'),
        (3, 'M'),
        (4, 'L'),
        (5, 'XL'),
        (6, 'XXL'),
    ]
    
    GENERO_CHOICES = [
        (1, 'Hombre'),
        (2, 'Mujer'),
        (3, 'Unisex'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='remeras/')
    marca = models.CharField(max_length=50)
    talle = models.PositiveSmallIntegerField(choices=TALLE_CHOICES)
    color = models.CharField(max_length=50)
    lisa = models.BooleanField(default=True)
    genero = models.PositiveSmallIntegerField(choices=GENERO_CHOICES)
    
    def __str__(self):
        return f"{self.nombre} - {self.marca} - {self.get_talle_display()} - {self.color}"


######carrito de compras########

class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Carrito de {self.usuario.username} creado el {self.fecha_creacion}'

class ElementoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='elementos', on_delete=models.CASCADE)
    remera = models.ForeignKey(Remera, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    def get_total_precio(self):
        return self.remera.precio * self.cantidad

    def __str__(self):
        return f'{self.cantidad} x {self.remera.nombre}'

    def get_total_precio(self):
        return self.cantidad * self.remera.precio