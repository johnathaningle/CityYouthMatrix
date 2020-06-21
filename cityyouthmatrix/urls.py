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
    add_user,
    get_drivers,
    get_family_trips
)
from cityyouthmatrix.apps.accounts.views import (
    dispatcher,
    driver,
    driver_notifications,
    driver_profile,
    driver_site_rules,
    driver_trip_info,
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
    manage_rules,
    new_trip
)

urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    # api section
    path("api/getdrivers", get_drivers),
    path("api/adddriver", add_driver),
    path("api/adduser", add_user),
    path("api/getfamilytrips", get_family_trips),
    # dispatcher section
    path("dispatcher/dispatcher", dispatcher),
    path("dispatcher/managedrivers", manage_drivers),
    path("dispatcher/managefamilies", manage_families),
    path("dispatcher/driverinfo", driver_info),
    path("dispatcher/familyinfo", family_info),
    path("dispatcher/managetrips", manage_trips),
    path("dispatcher/tripinfo", trip_info),
    path("dispatcher/broadcast", broadcast),
    path("dispatcher/notifications", notifications),
    path("dispatcher/profile", dispatcher_profile),
    path("dispatcher/rules", manage_rules),
    path("dispatcher/newtrip", new_trip),
    # driver section
    path("driver/driver", driver),
    path("driver/driver-notifications", driver_notifications),
    path("driver/driver-profile", driver_profile),
    path("driver/tripinfo", driver_trip_info),
    path("driver/driver-site-rules", driver_site_rules)
]
