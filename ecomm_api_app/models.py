from django.contrib.auth.models import AbstractUser  # Importing Django's built-in AbstractUser model
from django.db import models  # Importing Django's ORM models

class User(AbstractUser):
    # Extending the AbstractUser model to include a unique email field
    email = models.EmailField(unique=True)