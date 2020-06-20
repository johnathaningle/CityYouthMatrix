"""cityyouthmatrix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cityyouthmatrix.apps.api.views import (
    add_driver,
    get_drivers
)
from cityyouthmatrix.apps.accounts.views import (
    dispatcher,
    home, 
    manage_drivers,
    manage_families,
    family_info,
    driver_info,
    manage_trips,
    trip_info,
    broadcast,
    notifications,
    dispatcher_profile,
    manage_rules
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("dispatcher/dispatcher", dispatcher),
    path("dispatcher/managedrivers", manage_drivers),
    path("dispatcher/managefamilies", manage_families),
    path("dispatcher/driverinfo", driver_info),
    path("dispatcher/familyinfo", family_info),
    path("", home),
    path("api/getdrivers", get_drivers),
    path("api/adddriver", add_driver),
    path("dispatcher/managetrips", manage_trips),
    path("dispatcher/tripinfo", trip_info),
    path("dispatcher/broadcast", broadcast),
    path("dispatcher/notifications", notifications),
    path("dispatcher/profile", dispatcher_profile),
    path("dispatcher/rules", manage_rules),
]
