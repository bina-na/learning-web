# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
