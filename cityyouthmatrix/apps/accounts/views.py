from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def dispatcher(request: HttpRequest):
    return render(request, "accounts/dispatcher.html")

def home(request: HttpRequest):
    return render(request, "accounts/home.html")

def manage_drivers(request: HttpRequest):
    return render(request, "accounts/manage-drivers.html")

def manage_families(request: HttpRequest):
    return render(request, "accounts/manage-families.html")

def new_family(request: HttpRequest):
    return render(request, "accounts/new-family.html")

def new_driver(request: HttpRequest):
    return render(request, "accounts/new-driver.html")

