
from django import forms
from .models import Remera
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



#Formulario de producto

class RemeraForm(forms.ModelForm):
    class Meta:
        model = Remera
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'marca', 'talle', 'color', 'lisa', 'genero']


#Registro de usuario
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')