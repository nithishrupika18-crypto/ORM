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