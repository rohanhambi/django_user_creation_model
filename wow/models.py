from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class Person(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
