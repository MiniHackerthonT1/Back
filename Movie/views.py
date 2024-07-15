from django.shortcuts import render
from rest_framework.decorators import permission_classes
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializers import *
from rest_framework.decorators import api_view
# Create your views here.
class SaveDBAPI(APIView):
    # 영화 데이터를 json으로 받아서 DB에 저장
    def post(self, request):
        url = "https://port-0-minihackathon-12-lyec0qpi97716ac6.sel5.cloudtype.app/movie"
        res = requests.get(url)
        movies = res.json()['movies']
        for movie in movies:
            serializer = SaveMovieToDBSerializer(data=movie)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class searchMovieAPI(APIView):
    authentication_classes = [JWTAuthentication]

    @method_decorator(permission_classes([AllowAny]))
    def get(self, request, movieName):
        moviesKor = Movie.objects.filter(title_kor__contains=movieName) # title_kor이 movieName을 포함하는 영화
        moviesEng = Movie.objects.filter(title_eng__contains=movieName) # title_eng이 movieName을 포함하는 영화
        movies = moviesKor | moviesEng

        serializer = SearchMovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET']) # 영화 디테일
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
        if request.method =='GET':
            serializer = MovieDetailSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def comment(request, pk): # 댓글달기
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, movie=movie)
            movie_serializer = MovieDetailSerializer(movie)
            return Response(movie_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)