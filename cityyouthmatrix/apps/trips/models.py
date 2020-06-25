from django.db import models
from django.db.models import F
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField

from cityyouthmatrix.apps.accounts.models import Address


class ActivityPartner(models.Model):
    """
    An organization hosting the extra-curricular event and learning experience. 
    The location/destination information for a CYM-sponsored activity
    The location stores the address for activity-partner or CYM location.
    """
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True, help_text='Is the activity partner still active')

    def __str__(self):
        return self.name


class EventAddress(Address):
    pass


class Event(models.Model):
    """Every event takes place at an activity partner's location
    """

    class EventSeasons(models.TextChoices):
        SPRING = "Spring", ("Spring")
        SUMMER = "Summer", ("Summer")
        FALL = "Fall", ("Fall")
        WINTER = "Winter", ("Winter")

    name = models.CharField(max_length=200)
    activity_partner = models.ForeignKey(
        ActivityPartner,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        limit_choices_to={'is_active': True}
    )
    event_datetime = models.DateTimeField(help_text='The start date and time of the event')
    address = models.ForeignKey(EventAddress, on_delete=models.CASCADE)
    season = models.CharField(max_length=6, choices=EventSeasons.choices)

    def __str__(self):
        return f"{str(self.activity_partner) + ' - ' if self.activity_partner else ''}{self.name}"


class Trip(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    family = models.ForeignKey('accounts.Family', on_delete=models.CASCADE)
    passengers = ChainedManyToManyField(
        'accounts.FamilyMember',
        chained_field='family',
        chained_model_field='family',
        horizontal=False
    )
    pickup_address = ChainedForeignKey(
        'accounts.FamilyAddress',
        chained_field='family',
        chained_model_field='family',
        related_name='+',
        on_delete=models.DO_NOTHING,
    )
    pickup_location = models.CharField(max_length=100, blank=True, help_text='Specific pickup location at the address (front, side, etc)')
    pickup_datetime = models.DateTimeField(null=True, db_index=True, help_text='Date and time to pickup')
    pickup_completed = models.BooleanField(default=False, help_text='Was the family picked up and dropped off at the event')
    pickup_completed_datetime = models.DateTimeField(null=True, help_text='Date and time the family was dropped off at the event')
    pickup_driver = models.ForeignKey(
        'accounts.Driver',
        related_name='pickup_driver',
        on_delete=models.DO_NOTHING,
        limit_choices_to={'is_verified': True},
        null=True,
        blank=True,
    )
    pickup_driver_notes = models.CharField(max_length=500, blank=True, help_text='Notes about the pickup from the driver')
    pickup_family_notes = models.CharField(max_length=500, blank=True, help_text='Notes about the pickup from the family')

    return_address = ChainedForeignKey(
        'accounts.FamilyAddress',
        chained_field='family',
        chained_model_field='family',
        related_name='+',
        on_delete=models.DO_NOTHING,
    )
    return_datetime = models.DateTimeField(null=True, db_index=True, help_text='Date and time to return')
    return_completed = models.BooleanField(default=False, help_text='Was the family picked up and dropped off at the return address')
    return_completed_datetime = models.DateTimeField(null=True, help_text='Date and time the family was dropped off at the return address')
    return_driver = models.ForeignKey(
        'accounts.Driver',
        related_name='return_driver',
        on_delete=models.DO_NOTHING,
        limit_choices_to={'is_verified': True},
        null=True,
        blank=True,
    )
    return_driver_notes = models.CharField(max_length=500, blank=True, help_text='Notes about the return from the driver')
    return_family_notes = models.CharField(max_length=500, blank=True, help_text='Notes about the return from the family')

    is_cancelled = models.BooleanField(default=False, help_text='Was the trip cancelled')
    cancelled_datetime = models.DateTimeField(null=True, help_text='Date and time the trip was cancelled')

    car_seat_required = models.BooleanField(default=False)
    booster_seat_required = models.BooleanField(default=False)
    special_needs = models.CharField(max_length=300, blank=True, help_text='Any special needs of the family')

    next_required_datetime = models.DateTimeField(null=True, db_index=True, help_text='Internal field for sorting')

    class Meta(object):
        unique_together = ('event', 'family')
        ordering = [F('next_required_datetime').asc(nulls_last=True)]

    def __str__(self):
        return f'{self.family} {self.event.name} Trip'

    def save(self, *args, **kwargs):
        if self.is_cancelled and self.cancelled_datetime is None:
            self.cancelled_datetime = timezone.now()
        if not self.is_cancelled and self.cancelled_datetime is not None:
            self.cancelled_datetime = None
        if self.pickup_completed and self.pickup_completed_datetime is None:
            self.pickup_completed_datetime = timezone.now()
        if self.return_completed and self.return_completed_datetime is None:
            self.return_completed_datetime = timezone.now()

        if self.is_cancelled:
            self.next_required_datetime = None
        elif self.pickup_completed:
            self.next_required_datetime = self.return_datetime
        elif self.return_completed:
            self.next_required_datetime = None
        else:
            self.next_required_datetime = self.pickup_datetime

        super(Trip, self).save(*args, **kwargs)

    @property
    def is_available(self):
        return (
            not self.is_cancelled and
            (self.pickup_driver is None or self.return_driver is None) and
            not self.return_completed
        )

    @property
    def pickup_duration(self):
        if self.pickup_datetime is None or self.pickup_completed_datetime is None:
            return None
        return (self.pickup_completed_datetime - self.pickup_datetime).minutes

    @property
    def return_duration(self):
        if self.return_datetime is None or self.return_completed_datetime is None:
            return None
        return (self.return_completed_datetime - self.return_datetime).minutes
