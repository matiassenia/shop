from django.db import models

# Create your models here.

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
    talle = models.IntegerField(choices=TALLE_CHOICES)
    color = models.CharField(max_length=50)
    lisa = models.BooleanField(default=True)
    genero = models.IntegerField(choices=GENERO_CHOICES)
    
    def __str__(self):
        return self.nombre
