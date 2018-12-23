# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 200, null= False)
    descripcion = models.TextField(blank= False, null= False)
    fecha_creacion = models.DateField('Fecha creacion', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    id_autor = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField('Fecha creacion', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.nombre