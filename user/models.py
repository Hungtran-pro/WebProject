from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    sex_choice = ((0,"Male"),(1,"Female"),(2,"Other"))
    dob = models.CharField(max_length=250,default='')
    sex = models.CharField(max_length=250)
    address = models.CharField(max_length=255)
    avatar = models.CharField(max_length=250,default='')
    phone=models.CharField(max_length=11,default='')