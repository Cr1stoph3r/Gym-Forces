from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import CustomUserCreationForm, ContactoForm, GaleriaForm
from django.contrib.auth import authenticate, login
from .models import galeria
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import GaleriaSerializer

# Create your views here.

def error_facebook(request):
    return render(request, 'registration/error_facebook.html')

class GaleriaViewset(viewsets.ModelViewSet):
    queryset = galeria.objects.all()
    serializer_class = GaleriaSerializer

    def get_queryset(self):
        gale = galeria.objects.all()

        deporte = self.request.GET.get('deporte')

        if deporte:
            gale = gale.filter(deporte__contains=deporte)

        return gale


def index(request):
    gal = galeria.objects.all()
    data ={
        'gal' : gal
    }
    return render(request, 'main/index.html', data)

def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return render(request, 'main/index.html')
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)

def contacto(request):
    data = {
        'form' : ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario


    return render(request, 'main/contacto.html', data)

@permission_required('main.add_galeria')
def agregar_imagen(request):
    data = {
        'form' : GaleriaForm()
    }
    if request.method == 'POST':
        formulario = GaleriaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'main/galeria/agregar.html', data)

@permission_required('main.change_gsleria')
def modificar_imagen(request, id):
    gale = galeria.objects.get(id=id)
    data = {
        'form' : GaleriaForm(instance=gale)
    }
    if request.method == 'POST':
        formulario = GaleriaForm(data=request.POST, instance=gale, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
        data["form"] = formulario
    return render(request, 'main/galeria/modificar.html', data)

@permission_required('main.view_galeria')
def listar_imagen(request):
    gale = galeria.objects.all()
    data = {
        'gale' : gale
    }
    return render(request,'main/galeria/listar.html', data)

@permission_required('main.delete_galeria')
def eliminar_imagen(request, id):
    gale = get_object_or_404(galeria, id=id)
    gale.delete()
    return listar_imagen(request)