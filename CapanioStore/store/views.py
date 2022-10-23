from ast import Return
import re
from django.shortcuts import render

# Create your views here.

def store_view(request):
    return render(request, 'index.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def menu(request):
    return render(request, 'menu.html')

def about_us(request):
    return render(request, 'about_us.html')

def reservation(request):
    return render(request, 'reservation.html')
