from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework import serializers
from .models import Movie, Actor

class SaveActorToDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'character', 'image_url']

class SaveMovieToDBSerializer(serializers.ModelSerializer):
    actors = SaveActorToDBSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['actors', 'title_kor', 'title_eng', 'poster_url', 'genre', 'showtime', 'release_date', 'plot', 'rating', 'director_name', 'director_image_url']

    def create(self, validated_data):
        actorsData = validated_data.pop('actors')
        movie = Movie.objects.create(**validated_data)

        for actorData in actorsData:
            actor, created = Actor.objects.get_or_create(**actorData)
            movie.actors.add(actor)

        return "완료!"
    
class SearchMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title_kor', 'title_eng', 'poster_url', 'rating']