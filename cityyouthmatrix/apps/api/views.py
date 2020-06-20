from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from ..accounts.models import (
    Driver
)

# Create your views here.
def get_drivers(request: HttpRequest) -> JsonResponse:
    drivers = list(Driver.objects.values())
    return JsonResponse(drivers, safe=False)



@csrf_exempt
def add_driver(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        driver = Driver()
        driver.from_query_dict(request.POST)
        return JsonResponse({"success": True}, safe=False)
    else:
        return JsonResponse({"success": False}, safe=False)