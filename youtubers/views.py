from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from youtubers.models import Youtubers

# Create your views here.
def youtubers(request):
    alltubers = Youtubers.objects.order_by('-created_date')
    data ={
        'alltubers' : alltubers , 
    }

    return render(request ,'youtubers/youtubers.html', data)


def youtubers_detail(request ,id):
    tuber = get_object_or_404(Youtubers, pk =id )

    data={
        'tuber' : tuber ,
    }
    return render(request ,'youtubers/youtubers_details.html', data)


def search(request):
    pass 