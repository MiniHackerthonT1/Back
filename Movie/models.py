from django.db import models

# Create your models here.
class Movie(models.Model):
    actors = models.IntegerField(null=False)
    comment = models.IntegerField(null=False)
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100)
    poster_url = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    showtime = models.CharField(max_length=100)
    release_date = models.DateField(max_length=100)
    plot = models.CharField(max_length=1000)
    rating = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    director_image_url = models.CharField(max_length=500)