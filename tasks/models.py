from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.CharField(max_length=1000)
