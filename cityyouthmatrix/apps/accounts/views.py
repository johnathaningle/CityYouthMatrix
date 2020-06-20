from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def dispatcher(request: HttpRequest):
    return render(request, "accounts/dispatcher/dispatcher.html")

def home(request: HttpRequest):
    return render(request, "accounts/home.html")

def manage_drivers(request: HttpRequest):
    return render(request, "accounts/dispatcher/manage-drivers.html")

def manage_families(request: HttpRequest):
    return render(request, "accounts/dispatcher/manage-families.html")

def new_family(request: HttpRequest):
    return render(request, "accounts/dispatcher/new-family.html")

def new_driver(request: HttpRequest):
    return render(request, "accounts/dispatcher/new-driver.html")

def manage_trips(request: HttpRequest):
    return render(request, "accounts/dispatcher/manage-trips.html")    

def trip_info(request: HttpRequest):
    return render(request, "accounts/dispatcher/trip-info.html")    

def broadcast(request: HttpRequest):
    return render(request, "accounts/dispatcher/broadcast.html")    