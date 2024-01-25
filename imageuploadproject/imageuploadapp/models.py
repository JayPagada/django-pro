
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField() 
    image = models.ImageField(upload_to='blogs/images/')

class EmailData(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.TextField()
    email=models.EmailField(max_length=254,null=False)
