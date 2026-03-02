from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('IT-TEAM', 'It-team'),
        ('SUPPORT', 'Support'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username