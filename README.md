# Ex02 Django ORM Web Application
# Date:1/11/2026
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 cars

# PROGRAM
```
models.py

from django.db import models
from django.contrib import admin

class Student (models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    DOB=models.DateField()
    FatherName=models.CharField (max_length=20, null=True,blank=True)
    MotherName=models.CharField (max_length=20, null= True ,blank=True)
    phoneNumber=models.IntegerField(null=True,blank=True)
    marks=models.IntegerField(null=True,blank=True)
class StudentAdmin(admin. ModelAdmin):
    list_display=['Name','Age','DOB','FatherName','MotherName','phoneNumber','marks']

views.py

from django.shortcuts import render,HttpResponse
def home(request):
    return HttpResponse('<h1>hello world</h1>')
def about(request):
    return render(request,'dragon.html',{'name':'AK'})
# Create your views here.


```
# OUTPUT
![alt text](<Screenshot 2026-11-01 150135.png>)
![alt text](<Screenshot 2026-11-01 150152.png>)
# RESULT
Thus the program for creating a database using ORM hass been executed successfully
