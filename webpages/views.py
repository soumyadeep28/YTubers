from django.shortcuts import render
from webpages.models import Slider , Team 
from youtubers.models import Youtubers
# Create your views here.
def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtubers.objects.order_by('-created_date').filter(is_featured=True)
    youtubers = Youtubers.objects.order_by('-created_date')[:6]
    data ={
        'sliders' : sliders,
        'teams' : teams,
        'featured_youtubers' : featured_youtubers,
        'youtubers' : youtubers
    }
    return render(request , 'webpages/home.html' , data )

def about(request):
    teamdetails = Team.objects.order_by('-created_date')
    data = {
        'teams' : teamdetails,
    }
    return render(request , 'webpages/about.html' ,data) 


def services(request):
    return render(request, 'webpages/services.html')


def contacts(request):
    return render(request, 'webpages/contacts.html') 
    
