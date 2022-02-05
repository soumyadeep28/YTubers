from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=255)         #blank=true for it i want to keep blank
    subtitle = models.CharField(max_length=255)
    buttontext = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

