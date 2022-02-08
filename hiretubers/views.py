from django.contrib import messages
from django.shortcuts import redirect, render
from hiretubers.models import Hiretubers

'''
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

'''
# Create your views here.
def hiretubers(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id= request.POST['tuber_id']
        tuber_name= request.POST['tuber_name']
        email= request.POST['email']
        city= request.POST['city']
        phone= request.POST['phone']
        user_id= request.POST['user_id']
        msg= request.POST['msg']
        state= request.POST['state']

        hire = Hiretubers(
            first_name = first_name,
            last_name = last_name,
            tuber_id = tuber_id,
            tuber_name = tuber_name,
            email = email,
            city = city,
            phone = phone,
            user_id = user_id,
            msg = msg,
            state = state,
        )
        hire.save()
        messages.success(request , 'Thanks for reaching out' )
        return redirect('youtubers')
    else:
        messages.warning(request , 'Not submitted' )
        return redirect('youtubers')
    
