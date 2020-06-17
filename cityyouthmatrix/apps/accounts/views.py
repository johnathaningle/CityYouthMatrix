from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def dispatcher(request: HttpRequest):
    return render(request, "accounts/dispatcher.html")

def home(request: HttpRequest):
    return render(request, "accounts/home.html")