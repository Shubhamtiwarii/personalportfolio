from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()

class project(models.Model):
    projectname=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    description=models.CharField(max_length=150)
    link=models.CharField(max_length=150)