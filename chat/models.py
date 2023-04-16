from django.db import models


# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=55)
    message = models.TextField()
