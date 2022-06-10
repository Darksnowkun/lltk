from django.db import models
from django.contrib.auth.models import AbstractUser
from languages.models import languages

# Create your models here.

class MyUser(AbstractUser):
    registered_languages = models.ManyToManyField(languages)
    pass
