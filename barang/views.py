from django.http import HttpResponse
from django.shortcuts import render

from .models import barang


# Create your views here.
def home(request):
    data={}
    data['product']=barang.objects.all()
    return render(request,"./product/index.html",data)

