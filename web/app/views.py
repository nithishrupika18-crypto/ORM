from django.shortcuts import render,HttpResponse
def home(request):
    return HttpResponse('<h1>hello world</h1>')
def about(request):
    return render(request,'dragon.html',{'name':'AK'})
# Create your views here.
