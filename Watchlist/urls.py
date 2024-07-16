from django.urls import path
from .views import *
from . import views

app_name = 'Watchlist'

urlpatterns = [
    path('register/', registerWatchlistAPI.as_view()),
    path('getwatchlists/', getWatchlistAPI.as_view()),
]