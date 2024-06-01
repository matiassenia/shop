from django import forms
from .models import Remera

class RemeraForm(forms.ModelForm):
    class Meta:
        model = Remera
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'marca', 'talle', 'color', 'lisa', 'genero']
