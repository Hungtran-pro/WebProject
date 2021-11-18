from django.db import models
from django.forms.fields import CharField
from django.contrib.auth.models import AbstractUser
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
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} to {self.receiver.username}'