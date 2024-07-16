from django.db import models
from User.models import CustomUser

# Create your models here.
class Actor(models.Model):
    name = models.CharField(null=False, max_length = 50)
    character = models.CharField(null=False, max_length = 50)
    image_url = models.CharField(max_length=500)

class Movie(models.Model):
    # actors = models.IntegerField(null=False)
    # comment = models.IntegerField(null=False)
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
    actors = models.ManyToManyField(Actor)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE, related_name = "comments")
    user = models.ForeignKey(CustomUser, null = True, on_delete=models.CASCADE)
    content = models.TextField(default="")

class Reply(models.Model):
    movie = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, null = True, on_delete=models.CASCADE, related_name="replies")
    comment = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField(default="")
    
    

