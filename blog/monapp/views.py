from django.shortcuts import render
from .models import Livre

def index(request):
    livres = Livre.objects.all()
    return render(request, 'index.html', {'livres': livres})

def adminis(request):
    return render(request, 'adminis.html')


# Create your views here.
