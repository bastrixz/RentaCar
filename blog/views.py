from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, '../templates/inicio.html', {}) 

def contacto(request):
    return render(request, '../templates/contacto.html', {}) 

def galeria(request):
    return render(request, '../templates/galeria.html', {}) 

def nocuenta(request):
    return render(request, '../templates/nocuenta.html', {}) 

def promociones(request):
    return render(request, '../templates/promociones.html', {})

def registro(request):
    return render(request, '../templates/registro.html', {}) 
