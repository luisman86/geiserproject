from django.db import models

from .parent import log

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)

    def direcciones_cliente(self):
        log('Entra a direcciones_cliente', 'Info')
        direcciones = Direccion.objects.filter(cliente=self)
        log('Direcciones {}'.format(direcciones), 'Debug')
        for direccion in direcciones:
            log('Direccion: {}'.format(direccion), 'Debug')
            return '{} - {} - {}'.format(direccion.calle, direccion.num_ext, direccion.fraccionamiento)


class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    num_ext = models.IntegerField()
    num_int = models.IntegerField(blank=True, null=True)
    fraccionamiento = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=100, blank=True, null=True)
    comments = models.TextField(max_length=300, blank=True, null=True)


class Status(models.Model):
    nombre = models.CharField(max_length=100)


class Origen(models.Model):
    nombre = models.CharField(max_length=100)


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
