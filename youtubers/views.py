from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def youtubers(request):
    return HttpResponse("<h1> Youtubers home page </h1>")


def youtubers_detail(request ,id):
    pass 


def search(request):
    pass 