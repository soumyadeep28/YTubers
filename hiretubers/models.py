from django.db import models
# Create your models here.
class Hiretubers(models.Model):
    first_name =models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    tuber_id =models.IntegerField( blank=True)
    tuber_name =models.CharField(max_length=100)
    email =models.EmailField(max_length=255)
    city =models.CharField(max_length=255)
    phone = models.IntegerField()
    user_id = models.CharField(max_length=255 , blank=True)
    created_At = models.DateTimeField(auto_now_add=True)
    msg = models.TextField()
    state =models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.email


    

