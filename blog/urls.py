from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('galeria', views.galeria, name='galeria'),
    path('promociones', views.promociones, name='promociones'),
    path('registro', views.registro, name='registro'),
    path('', include('django.contrib.auth.urls')),
    path('nocuenta', views.SignUp.as_view(), name='nocuenta'),
    path('autoregistro', views.autoregistro, name='autoregistro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


