from django.contrib import admin
from .models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','name','title','picture','category','created_at','updated_at']
admin.site.register(Image,ImageAdmin) 
