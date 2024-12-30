from django.contrib.auth.models import AbstractUser  # Importing Django's built-in AbstractUser model
from django.db import models  # Importing Django's ORM models

class User(AbstractUser):
    # Extending the AbstractUser model to include a unique email field
    email = models.EmailField(unique=True)
    first_name = models.CharField(default='first_name null')
    last_name = models.CharField(default='last_name null')
    phonenumber = models.CharField(default='phonenumber null')
    address = models.CharField(default='address null')