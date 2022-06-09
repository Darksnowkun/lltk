from django.db import models

# Create your models here.

class languages(models.Model):
    language = models.CharField(max_length=127, help_text="Name of Language")

