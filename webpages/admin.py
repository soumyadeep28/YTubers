from django.contrib import admin
from webpages import models
from django.utils.html import format_html 
#---------MODIFICATION of admin pannel --------------------->
class TeamAdmin(admin.ModelAdmin):
    def myphoto(self ,object):
        
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id' , 'myphoto','first_name' , 'last_name' ,'role' , 'created_date')
    list_display_links = ('id' , 'first_name' , 'last_name' )       #this to make the options clickable
    search_fields =('id' ,'first_name' ,'role')
    list_filter = ('role',)


class Sliderpannel(admin.ModelAdmin):
    def myphoto(self ,object):
        
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))


    list_display = ( 'headline' , 'buttontext' , 'myphoto' )
# Register your models here.
admin.site.register(models.Slider , Sliderpannel)    
admin.site.register(models.Team , TeamAdmin)
