from django.db import models


class Auto(models.Model):
    modelo = models.CharField(max_length=200, default='', blank=False)
    anio = models.IntegerField()
    color = models.CharField(max_length=200, default='')
    stock = models.BooleanField(default=False)
    marca = models.CharField(max_length=200, default='')
    imagen = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.modelo


