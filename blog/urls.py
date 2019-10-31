from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('galeria', views.galeria, name='galeria'),
    path('nocuenta', views.nocuenta, name='nocuenta'),
    path('promociones', views.promociones, name='promociones'),
    path('registro', views.registro, name='registro'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

