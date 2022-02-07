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

    city_values = Youtubers.objects.values_list('city', flat=True).distinct()   #it gives key value pair and array
    camera_type_values = Youtubers.objects.values_list('camera_type', flat=True).distinct()
    category_values = Youtubers.objects.values_list('category', flat=True).distinct()
    
    #-------for filtering out the keyword values from the list
    if 'keyword' in request.GET :
        keyword = request.GET['keyword']
        if keyword :
            tubers = tubers.filter(description__icontains=keyword )
    #-------for filtering out the city values from the array
    if 'city' in request.GET :
        city = request.GET['city']
        if city :
            tubers = tubers.filter(city__iexact = city)

    if 'camera_type' in request.GET :
        camera_type = request.GET['camera_type']
        if camera_type :
            tubers = tubers.filter(camera_type__iexact = camera_type)


    if 'category' in request.GET :
        category = request.GET['category']
        if category :
            tubers = tubers.filter(category__iexact = category)

    data ={
        'alltubers' : tubers,
        'city' : city_values,
        'camera' : camera_type_values,
        'category' : category_values
    }
    return render(request ,'youtubers/search.html' ,data ) 