from django.contrib import admin
from .models import (
    ActivityPartner,
    Event,
    EventAddress,
    Trip,
)
from cityyouthmatrix.apps.accounts.models import FamilyMember


class ActivityPartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity_partner', 'event_datetime', 'address', 'season')
    list_select_related = True
    list_filter = ('activity_partner', 'season')


class TripAdmin(admin.ModelAdmin):
    list_display = ('event', 'family', 'pickup_driver', 'return_driver', 'is_available')
    list_select_related = True
    list_filter = ('event', 'family', 'pickup_driver', 'return_driver', 'pickup_completed', 'return_completed', 'is_cancelled')
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
admin.site.register(Event, EventAdmin)
admin.site.register(EventAddress)
admin.site.register(ActivityPartner, ActivityPartnerAdmin)
