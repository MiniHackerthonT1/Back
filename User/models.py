from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []
    email = None
    username = models.CharField(max_length=100, unique = True) #회원가입 시 아이디
    nickname = models.CharField(max_length=100)

