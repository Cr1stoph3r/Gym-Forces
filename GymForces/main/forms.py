from django import forms
from .models import contacto, galeria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class loginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()

class ContactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ['nombre', 'email', 'deporte_consulta', 'mensaje', 'avisos']

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = galeria
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]