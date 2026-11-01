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
