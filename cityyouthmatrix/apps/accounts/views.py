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

def family_info(request: HttpRequest):
    return render(request, "accounts/dispatcher/family-info.html")

def driver_info(request: HttpRequest):
    return render(request, "accounts/dispatcher/driver-info.html")

def manage_trips(request: HttpRequest):
    return render(request, "accounts/dispatcher/manage-trips.html")    

def trip_info(request: HttpRequest):
    return render(request, "accounts/dispatcher/trip-info.html")    

def broadcast(request: HttpRequest):
    return render(request, "accounts/dispatcher/broadcast.html")   

def notifications(request: HttpRequest):
    return render(request, "accounts/dispatcher/notifications.html")  

def dispatcher_profile(request: HttpRequest):
    return render(request, "accounts/dispatcher/profile.html")     

def manage_rules(request: HttpRequest):
    return render(request, "accounts/dispatcher/rules.html")     

def new_trip(request: HttpRequest):
    return render(request, "accounts/dispatcher/new-trip.html")

#driver views
def driver(request: HttpRequest):
    return render(request, "accounts/driver/driver.html")

def driver_profile(request: HttpRequest):
    return render(request, "accounts/driver/driver-profile.html")

def driver_notifications(request: HttpRequest):
    return render(request, "accounts/driver/notifications.html")

def driver_site_rules(request: HttpRequest):
    return render(request, "accounts/driver/site-rules.html")

def driver_trip_info(request: HttpRequest):
    return render(request, "accounts/driver/trip-info.html")