from ast import Return
import re
from django.shortcuts import render
from store.models import Producto

# Create your views here.

def store_view(request):
    return render(request, 'index.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def menu(request):
    productos_segundos = Producto.objects.filter(categoria="001")
    productos_caldos = Producto.objects.filter(categoria="004")
    productos_postres = Producto.objects.filter(categoria="003")
    productos_bebidas = Producto.objects.filter(categoria="002")
    context = {'productos':productos_segundos, 'productos2':productos_caldos, 'productos3':productos_postres, 'productos4':productos_bebidas}
    return render(request, 'menu.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def reservation(request):
    return render(request, 'reservation.html')
