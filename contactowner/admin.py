from django.contrib import admin
from contactowner.models import Connect
# Register your models here.

class Connectpannel(admin.ModelAdmin):
    list_display = ('name' , 'number' , 'email' , 'subject')


admin.site.register(Connect , Connectpannel)
