from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Q


class ActivityPartner(models.Model):
    """
    An organization hosting the extra-curricular event and learning experience. 
    The location/destination information for a CYM-sponsored activity
    The location stores the address for activity-partner or CYM location.
    """
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class Event(models.Model):
    """Every event takes place at an activity partner's location
    """

    class EventSeasons(models.TextChoices):
        SPRING = "Spring", _("Spring")
        SUMMER = "Summer", _("Summer")
        FALL = "Fall", _("Fall")
        WINTER = "Winter", _("Winter")

    name = models.CharField(max_length=200)
    activity_partner = models.ForeignKey(ActivityPartner, on_delete=models.DO_NOTHING)
    event_datetime = models.DateTimeField()
    address = models.ForeignKey('accounts.Address', on_delete=models.CASCADE)
    season = models.CharField(max_length=6, choices=EventSeasons.choices)

    def __str__(self):
        return self.name
    


class Trip(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    family = models.ForeignKey('accounts.Family', on_delete=models.CASCADE)
    passengers = models.ForeignKey(
        'accounts.FamilyMember', on_delete=models.CASCADE)

    pickup_address = models.ForeignKey(
        'accounts.FamilyAddress', related_name='+', on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100, blank=True)
    pickup_datetime = models.DateTimeField(null=True, db_index=True)
    pickup_completed = models.BooleanField(default=False)
    pickup_driver = models.ForeignKey('accounts.Driver', related_name='pickup_driver', on_delete=models.DO_NOTHING)
    pickup_driver_notes = models.CharField(max_length=500, blank=True)
    pickup_family_notes = models.CharField(max_length=500, blank=True)

    return_address = models.ForeignKey(
        'accounts.FamilyAddress', on_delete=models.CASCADE, related_name='+')
    return_datetime = models.DateTimeField(null=True, db_index=True)
    return_completed = models.BooleanField(default=False)
    return_driver = models.ForeignKey('accounts.Driver', related_name='return_driver', on_delete=models.DO_NOTHING)
    return_driver_notes = models.CharField(max_length=500, blank=True)
    return_family_notes = models.CharField(max_length=500, blank=True)

    is_cancelled = models.BooleanField(default=False)
    cancelled_datetime = models.DateTimeField(null=True)

    car_seat_required = models.BooleanField(default=False)
    booster_seat_required = models.BooleanField(default=False)
    special_needs = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.event.name} Trip"

    @property
    def is_available(self):
        return (
            not self.is_cancelled and
            (self.pickup_driver is None or self.return_driver is None) and
            not self.return_completed
        )
