from django.contrib import messages
from django.shortcuts import redirect, render
from contactowner.models import Connect
# Create your views here.

def connectus(request):
    if request.method == "POST" :
        name = request.POST["name"]
        number = request.POST["number"]
        email = request.POST["email"]
        company = request.POST["company"]
        subject = request.POST["subject"]
        msg = request.POST["msg"] 
        cnt = Connect(
            name  = name,
            number = number,
            email = email,
            company = company,
            subject = subject,
            msg = msg,

        )
        cnt.save() 
        messages.success(request , "Successfully submitted the Form")
        redirect('contacts')

    return redirect('youtubers')
