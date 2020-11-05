from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Producto

class Productoform(forms.ModelForm):
    class Meta:
        model = Producto
        fields=[
            'Codigo',
            'Nombre',
            'Descripcion',
            'Precio_de_venta',
            'URL_Video',
            'URL_Imagen'
        ]
        labels= {
            'Codigo' : 'Código',
            'Nombre' : 'Nombre' ,
            'Descripcion' : 'Descripción',
            'Precio_de_venta' : 'Precio de venta',
            'URL_Video' : 'URL de Video',
            'URL_Imagen': 'URL de Imagen'
        }
        widgets = {
            'Codigo' : forms.TextInput(attrs={'class':'form-control'}),
            'Nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'Descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            'Precio_de_venta' : forms.TextInput(attrs={'class':'form-control'}),
            'URL_Video' : forms.TextInput(attrs={'class':'form-control'}),
            'URL_Imagen' : forms.TextInput(attrs={'class':'form-control'}),
        }
        
class Registroform(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',

        ]
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombre de pila',
            'last_name' : 'Apellidos',
            'email' : 'Correo electronico',

        }