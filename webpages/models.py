from django.db import models
from django.utils import timezone

# Create your models here.

class Team(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateTimeField(default=timezone.now)
    

class Slider(models.Model):
    headline = models.CharField(max_length=255)         #blank=true for it i want to keep blank
    subtitle = models.CharField(max_length=255)
    buttontext = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.headline

