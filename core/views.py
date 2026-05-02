from django.shortcuts import render
from core.models import *

def home(request):
    return render(request, 'index.html')

def movies(request):
    movies = Movies.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
def shows(request):
    shows = Shows.objects.all()
    return render(request, 'shows.html', {'shows': shows})