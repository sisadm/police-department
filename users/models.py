from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrator'),
        ('PO', 'Police Officer'),
    ]
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=55, unique=True)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)

    REQUIRED_FIELDS = ['email', 'role']

    def __str__(self):
        return self.username

