from youtubers import views
from django.urls import path 

urlpatterns = [
    path('', views.youtubers , name='youtubers'),
    path('<int:id>', views.youtubers_detail , name='youtubers_detail'),
    path('search', views.search  , name='search'),
]