from django.contrib import admin
from .models import ActivityPartner, Dispatcher, Driver, DriverNote, Family, FamilyMember, Trip
# Register your models here.

admin.site.register(Driver)
admin.site.register(DriverNote)

admin.site.register(Trip)
admin.site.register(Family)
admin.site.register(FamilyMember)
admin.site.register(ActivityPartner)
admin.site.register(Dispatcher)
