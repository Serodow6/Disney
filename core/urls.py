from django.urls import path
from core.views import *
app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('movies/', movies, name='movies'),
    path('shop/', shop, name='shop'),
    path('shows/', shows, name='shows'),
]