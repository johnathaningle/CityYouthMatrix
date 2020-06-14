from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Q


class User(AbstractUser):
    pass


class Address(models.Model):
    address_1 = models.CharField(max_length=300)
    address_2 = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)


class Driver(models.Model):
    """Picks up or returns family and child(ren)
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=9)


class Family(models.Model):

    class FamilyLanguages(models.TextChoices):
        ENGLISH = "EN", _("English")
        SPANISH = "ES", _("Spanish")

    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE)
    preferred_language = models.CharField(
        max_length=2, choices=FamilyLanguages.choices)


class FamilyAddress(Address):
    models.ForeignKey(Family, on_delete=models.CASCADE)


class FamilyMember(models.Model):

    class FamilyMemberTypes(models.TextChoices):
        CHILD = "C", _("Child")
        ADULT = "A", _("Adult")
        TAG_ALONG = "T", _("TagAlong")

    member_type = models.CharField(
        max_length=1,
        choices=FamilyMemberTypes.choices
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    @property
    def display_name(self):
        if self.member_type == FamilyMemberTypes.CHILD:
            return f'{self.first_name} {self.last_name[0]}.'
        else:
            return f'{self.first_name} {self.last_name}'


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
    activity_partner = models.ForeignKey(ActivityPartner, on_delete=models.DO_NOTHING)
    event_datetime = models.DateTimeField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Trip(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    passengers = models.ForeignKey(
        FamilyMember, on_delete=models.CASCADE)

    pickup_address = models.ForeignKey(
        FamilyAddress, related_name='+', on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100, blank=True)
    pickup_datetime = models.DateTimeField(null=True, db_index=True)
    pickup_completed = models.BooleanField(default=False)
    pickup_driver = models.ForeignKey(Driver, related_name='pickup_driver', on_delete=models.DO_NOTHING)
    pickup_driver_notes = models.CharField(max_length=500, blank=True)
    pickup_family_notes = models.CharField(max_length=500, blank=True)

    return_address = models.ForeignKey(
        FamilyAddress, on_delete=models.CASCADE, related_name='+')
    return_datetime = models.DateTimeField(null=True, db_index=True)
    return_completed = models.BooleanField(default=False)
    return_driver = models.ForeignKey(Driver, related_name='return_driver', on_delete=models.DO_NOTHING)
    return_driver_notes = models.CharField(max_length=500, blank=True)
    return_family_notes = models.CharField(max_length=500, blank=True)

    is_cancelled = models.BooleanField(default=False)
    cancelled_datetime = models.DateTimeField(null=True)

    car_seat_required = models.BooleanField(default=False)
    booster_seat_required = models.BooleanField(default=False)
    special_needs = models.CharField(max_length=300, blank=True)

    @property
    def is_available(self):
        return (
            not self.is_cancelled and
            (self.pickup_driver is None or self.return_driver is None) and
            not self.return_completed
        )
