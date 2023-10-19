from django.db import models
# from .serializers import RegisterSerializer
from django.contrib.auth.models import User



class Image(models.Model):
 def nameFile(instance, filename):
  return '/'.join(['images',str(instance.name),filename])
 name= models.CharField(max_length=200, default="")
 title = models.CharField(max_length=100,default="")
 description = models.TextField(default="")
 category = models.CharField(max_length=50,)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 picture= models.ImageField(upload_to=nameFile, blank=True)
# RegisterSerializer = models.ForeignKey(RegisterSerializer, on_delete=models.CASCADE)
 User=models.ForeignKey(User, on_delete=models.CASCADE,default="")
    

 

    