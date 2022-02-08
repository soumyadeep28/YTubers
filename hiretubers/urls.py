from django.urls import path 
from . import views

urlpatterns = [
    path('hire/' , views.hiretubers , name='hire'),
]