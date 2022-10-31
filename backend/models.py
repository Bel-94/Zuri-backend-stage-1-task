from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

class User(AbstractUser):
    slackUsername = models.CharField(max_length=30)
    backend = models.BooleanField(default=False)
    age = models.IntegerField()
    bio = models.CharField(max_length=100)
