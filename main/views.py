from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def buy(request):
    return render(request,'buy.html')

def rent(request):
    return render(request, 'rent.html')

def about(request):
    return render(request, 'about.html')