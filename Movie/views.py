from django.shortcuts import render
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

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