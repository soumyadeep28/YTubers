from django.shortcuts import render
from webpages import models 
# Create your views here.
def home(request):
    sliders = models.Slider.objects.all()
    data ={
        'sliders' : sliders
    }
    return render(request , 'webpages/home.html' , data )

def about(request):
    return render(request , 'webpages/about.html') 


def services(request):
    return render(request, 'webpages/services.html')


def contacts(request):
    return render(request, 'webpages/contacts.html') 
