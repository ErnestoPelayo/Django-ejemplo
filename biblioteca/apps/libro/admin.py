# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Autor, Libro

# Register your models here.

admin.site.register(Autor)
admin.site.register(Libro)