from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Administrator'),
        ('PO', 'Police Officer'),
    ]

    role = models.CharField(max_length=5, choices=ROLE_CHOICES)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

