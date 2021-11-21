from django.db import models
from django.forms.fields import CharField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
from user.models import MyUser

class Message(models.Model):
    sender = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='sender_messages'
    )
    receiver = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='receiver_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.datetime.now())
    
    def __str__(self):
        return f'{self.sender.username} to {self.receiver.username}'

