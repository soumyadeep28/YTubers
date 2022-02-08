from django.contrib import admin
from . import models

class HirePannel(admin.ModelAdmin):
    list_display=('first_name' , 'tuber_name' , 'email' ,'phone' )
    list_display_links = ( 'first_name' , 'tuber_name' , 'email')


admin.site.register(models.Hiretubers , HirePannel)
# Register your models here.
