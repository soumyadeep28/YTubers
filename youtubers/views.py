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
    tubers = Youtubers.objects.order_by('-created_date')
    if 'keyword' in request.GET :
        keyword = request.GET['keyword']
        if keyword :
            tubers = tubers.filter(description__icontains=keyword )
    data ={
        'alltubers' : tubers
    }
    return render(request ,'youtubers/search.html' ,data ) 