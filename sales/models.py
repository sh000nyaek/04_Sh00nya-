from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Sales_Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class sale(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Sales_Agent", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contactus(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name







