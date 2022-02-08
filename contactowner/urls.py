from django.urls import path
from contactowner import views 

urlpatterns = [ 
    path('contactus/' ,  views.connectus ,name='contactus'),
]