from django.contrib import admin
from .models import (
    ActivityPartner,
    Event,
    EventAddress,
    Trip,
)
from cityyouthmatrix.apps.accounts.models import FamilyMember


class TripAdmin(admin.ModelAdmin):
    readonly_fields = ('pickup_completed_datetime', 'return_completed_datetime', 'cancelled_datetime')
    fieldsets = (
        (None, {
            'fields': (
                'event', 'family', 'passengers', 'car_seat_required',
                'booster_seat_required', 'special_needs', 'is_cancelled',
                'cancelled_datetime'
            )
        }),
        (('Pickup'), {
            'fields': (
                'pickup_driver', 'pickup_address', 'pickup_location', 'pickup_datetime',
                'pickup_completed', 'pickup_completed_datetime', 'pickup_driver_notes',
                'pickup_family_notes'
            ),
        }),
        (('Return'), {
            'fields': (
                'return_driver', 'return_address', 'return_datetime',
                'return_completed', 'return_completed_datetime', 'return_driver_notes',
                'return_family_notes'
            )
        }),
    )

admin.site.register(Trip, TripAdmin)
admin.site.register(Event)
admin.site.register(EventAddress)
admin.site.register(ActivityPartner)
