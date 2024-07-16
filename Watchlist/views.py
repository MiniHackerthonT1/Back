from django.shortcuts import render
from rest_framework.decorators import permission_classes,  authentication_classes
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Movie

# Create your views here.
class registerWatchlistAPI(APIView):
    def post(self, request):
        print(request)
        movieId = request.movieId
        movie = Movie.objects.get(pk=movieId)
        user = request.user

        serializer = RegisterWatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user, movie=movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)