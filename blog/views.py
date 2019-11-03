from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import AutoForm
from .models import Auto


# Create your views here.
def inicio(request):
    return render(request, '../templates/inicio.html', {}) 

def contacto(request):
    return render(request, '../templates/contacto.html', {}) 

def galeria(request):
    autos = Auto.objects.all()
    return render(request, '../templates/galeria.html', {'autos': autos}) 

def nocuenta(request):
    return render(request, '../templates/nocuenta.html', {}) 

def promociones(request):
    return render(request, '../templates/promociones.html', {})

def registro(request):
    return render(request, '../templates/registro.html', {}) 

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'nocuenta.html'

def autoregistro(request):
    if request.method == "POST":
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = AutoForm()
    return render(request, '../templates/autoregistro.html', {'form': form})
