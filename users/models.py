from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # since we override USERNAME_FIELD
    
    ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('staff', 'Staff'),
    ('user', 'User'),
    
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')


    def __str__(self):
        return self.email

