from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Connect(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    email = models.EmailField()
    company = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    msg = RichTextField()

    def __str__(self) -> str:
        return self.name


