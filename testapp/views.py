# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Name

# Create your views here.


def list(request):
    names=Name.objects.all()
    return render(request,'list.html',{'names':names})