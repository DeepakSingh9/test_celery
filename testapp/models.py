# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Name(models.Model):
    name=models.CharField(max_length=20,blank=True)
    email=models.EmailField()

    def __str__(self):
        return self.name
