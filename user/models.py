from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    sex_choice = ((0,"nu"),(1,"nam"),(2,"khong"))
    age = models.CharField(max_length=250)
    sex = models.IntegerField(choices=sex_choice, default=0)
    address = models.CharField(max_length=255)