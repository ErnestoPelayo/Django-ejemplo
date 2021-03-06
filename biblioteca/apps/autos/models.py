# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Marca (models.Model):
    id = models.AutoField(primary_key = True, blank = False, null = False)
    nombre = models.CharField('Nombre', max_length = 200, blank = False, null = False)
    descripcion = models.CharField(max_length =200, blank = False, null = False)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


    def __str__(self):
        return self.nombre