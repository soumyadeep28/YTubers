from django.contrib import admin
from youtubers import models
from django.utils.html import format_html

#creating class so that we cna modify that in the admin pannel 
class YTadmin(admin.ModelAdmin):
    def myphoto(self , objects):
        return format_html("<img src='{}' , width='40'/>".format(objects.photo.url))
    list_display = ('id' ,'name' ,'myphoto' ,  'price' ,'is_featured')
    list_display_links = ('id' , 'name' )
    search_fields = ('name' ,'camera' )
    list_filter = ('city' , 'camera_type' , 'category')
    list_editable = ('is_featured',)




# Register your models here.
admin.site.register(models.Youtubers , YTadmin)
