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
from django.db import models
from django.contrib import admin



class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)

class Food(models.Model):
    food_name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE
    )
    def __str__(self):
        return self.food_name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE
    )
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    total_amount = models.FloatField()
    status = models.CharField(max_length=50,default="Pending")



```
# OUTPUT
![Output](Screenshot%2026-11-21%180319.png)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
