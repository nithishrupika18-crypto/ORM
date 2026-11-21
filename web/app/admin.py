from django.contrib import admin
from django.contrib import admin
from .models import Restaurant, Food, Customer, Order

from django.contrib import admin
from .models import Restaurant, Food, Customer, Order


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
  list_display = (
      "id",
      "phone_number",
  )  # 'name' field இருந்தா ('id', 'name', 'phone_number')-னு மாத்திக்கோ


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
  list_display = ("id", "food_name", "price", "restaurant")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "phone_number", "address")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = (
      "id",
      "customer",
  )  