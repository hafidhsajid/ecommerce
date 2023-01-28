from django.http import HttpResponse
from django.shortcuts import render

from .models import barang


# Create your views here.
def home(request):
    model=barang.objects.all()
    return HttpResponse(model)

