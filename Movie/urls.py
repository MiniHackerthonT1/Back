from django.urls import path
from .views import *
from . import views

app_name = 'Movie'

urlpatterns = [
    path('home/<int:pageIdx>/', homeMovieAPI.as_view()),
    path('saveDB/', SaveDBAPI.as_view()),
    path('search/<str:movieName>/', searchMovieAPI.as_view()),
    path('movie_detail/<int:pk>/', movie_detail),
    path('movie_detail/<int:pk>/comment/',comment),
    path('movie_detail/deleteComment/<int:commentId>/', deleteCommentAPI.as_view()),
    path('movie_detail/reply/', saveReplyAPI.as_view()),
    path('movie_detail/deleteReply/<int:replyId>/', deleteReplyAPI.as_view()),
]