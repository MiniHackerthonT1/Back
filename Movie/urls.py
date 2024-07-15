from django.urls import path
from .views import *
from . import views

app_name = 'Movie'

urlpatterns = [
    path('home/<int:pageIdx>/', homeMovieAPI.as_view()),
    path('saveDB/', SaveDBAPI.as_view()),
    path('search/<str:movieName>/', searchMovieAPI.as_view()),
]