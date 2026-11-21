from django.shortcuts import render,HttpResponse
def home(request):
    return HttpResponse('<h1>hello world</h1>')
def about(request):
    return render(request,'dragon.html',{'name':'AK'})
# Create your views here.
from django.shortcuts import render
from .models import Restaurant, Food, Order


def dashboard(request):
    restaurants = Restaurant.objects.all()
    foods = Food.objects.all()
    orders = Order.objects.all()

    return render(
        request,
        "dashboard.html",
        {
            "restaurants": restaurants,
            "foods": foods,
            "orders": orders,
        },
    )