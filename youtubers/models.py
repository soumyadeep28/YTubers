from datetime import datetime
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Youtubers(models.Model):
    #-----------------choices-------------------------canon
    CITY = (
        ('BLR','Bangalore' ),
        ('HYD' , 'Hydrabad')
    )

    crew_choices = (
        ('solo' ,'solo'),
        ('small' ,'small'),
        ('large' ,'large'),
    )


    camera_choices = (
        ('canon' ,'canon'),
        ('Nikon' ,'Nikon'),
        ('Mobile' ,'Mobile'),
        ('Fujiki' ,'Fujiki'),
        ('GoPro' ,'GoPro'),
        ('other' ,'other'),
    )

    catagory_choices = (
        ('mobile Review' ,'mobile Review'),
        ('blog' ,'blog'),
        ('comedy' ,'comedy'),
        ('gamming' ,'gamming'),
        ('flimmaking' ,'flimmaking'),
        ('cooking' ,'cooking'),
        ('food Blog' ,'food Blog'),
        ('other' ,'other'),
    )



    #---------------------------Models------------------------------------
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/youtubers/%Y')
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255 ,choices=CITY)
    age = models.IntegerField()
    height = models.IntegerField()
    crew =models.CharField(max_length=255 , choices=crew_choices)
    camera_type = models.CharField(max_length=10 , choices=camera_choices)
    subs_count = models.IntegerField()
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now , blank=True )


