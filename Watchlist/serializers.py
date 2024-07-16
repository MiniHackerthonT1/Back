from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework import serializers
from .models import Watchlist

class RegisterWatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = ['user', 'movie']