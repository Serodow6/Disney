from django.shortcuts import render, get_object_or_404
from core.models import *

def home(request):
    news = News.objects.all()
    wod = Wod.objects.all()
    parks = Parks.objects.all()
    shows = Shows.objects.all()
    movies = Movies.objects.all()
    context = {
        'news': news
        , 'wod': wod
        , 'parks': parks
        , 'shows': shows
        , 'movies': movies
    }
    return render(request, 'index.html', context)

def movies(request):
    movies = Movies.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
        
def shows(request):
    shows = Shows.objects.all()
    familyshows = Familyshows.objects.all()
    concertandevents = Concertandevents.objects.all()
    return render(request, 'shows.html', {
        'shows': shows,
        'familyshows': familyshows,
        'concertandevents': concertandevents,
    })

def shopping(request):
    category = request.GET.get('category', '').strip()
    if category:
        products = Product.objects.filter(category__iexact=category)
    else:
        products = Product.objects.all()
    return render(request, 'shopping.html', {
        'products': products,
        'selected_category': category,
    })

def readmore(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'readmore.html', {'product': product})