from django.contrib import admin
from .models import (
    ActivityPartner,
    Event,
    Trip,
)

admin.site.register(Trip)
admin.site.register(Event)
admin.site.register(ActivityPartner)
