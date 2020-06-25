from typing import List

from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from cityyouthmatrix.common.view_models import SerializedTrip
from ..trips.models import Trip

from ..accounts.models import (
    Driver, Family, User
)

# Create your views here.
def get_drivers(request: HttpRequest) -> JsonResponse:
    drivers = list(Driver.objects.values())
    return JsonResponse(drivers, safe=False)


@csrf_exempt
def add_user(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        user = User()
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.contact_number = request.POST.get("contact_number")
        user.email = request.POST.get("email")
        user.save()
        user_id = User.objects.filter(
            contact_number = user.contact_number,
            last_name = user.last_name,
            first_name = user.first_name
        ).values("id").get()
        return JsonResponse({"success": True, "user_id": user_id})
    else:
        return JsonResponse({"success": False})

@csrf_exempt
def add_driver(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        driver = Driver()
        driver.is_verified = bool(request.POST.get("is_verified", False))
        driver.car_make = request.POST.get("car_make", "")
        driver.car_model = request.POST.get("car_model", "")
        driver.license_plate = request.POST.get("license_plate", "")
        driver.user = User.objects.filter(pk = request.POST.get("user_id")).get()
        driver.save()
        return JsonResponse({"success": True}, safe=False)
    else:
        return JsonResponse({"success": False}, safe=False)

def get_family_trips(request: HttpRequest):
    families = list(Family.objects.values())
    return JsonResponse(families, safe=False)

# @login_required
def get_driver_context(request:HttpRequest):
    managed_trips = list(Trip.objects.filter(pickup_driver__user__email=request.user.email).all())
    unassigned_trips = list(
        Trip.objects.filter(return_completed=False) |
        Trip.objects.filter(pickup_completed=False))

    managed_trips_context = [SerializedTrip(t).to_json() for t in managed_trips]
    unassigned_trips_context = [SerializedTrip(t).to_json() for t in unassigned_trips]

    context = {
        "managed_trips": managed_trips_context,
        "unassigned_trips": unassigned_trips_context
    }
    return JsonResponse(context, safe=False)