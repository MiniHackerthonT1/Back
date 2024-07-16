from django.db import models
from User.models import CustomUser
from Movie.models import Movie

# Create your models here.
class Watchlist(models.Model):
    movie = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE, related_name = "+")
    user = models.ForeignKey(CustomUser, null = True, on_delete=models.CASCADE, related_name="watchlists")