from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models


class Driver(models.Model):
    """Picks up or returns family and child(ren)
    """
    user_id = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)


class DriverNote(models.Model):
    """Drivers must be able to:
    Notate trips (Issues, concerns, positive experiences) 
    """
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=500)


class Trip(models.Model):

    # todo - make this foreign key to a location entity?
    pickup_location = models.CharField(max_length=300)
    pickup_completed = models.BooleanField(default=False)
    pickup_driver = models.ForeignKey(
        Driver, on_delete=models.DO_NOTHING, related_name="PickupDriver")

    # todo - make this foreign key to a location entity?
    return_location = models.CharField(max_length=300)
    return_complted = models.BooleanField(default=False)
    return_driver = models.ForeignKey(
        Driver, on_delete=models.DO_NOTHING, related_name="ReturnDriver")


class Family(models.Model):
    description = models.CharField(max_length=300, null=True)


class FamilyMember(models.Model):

    class FamilyMemberTypes(models.TextChoices):
        CHILD = "C", _("Child")
        ADULT = "A", _("Adult")
        TAG_ALONG = "T", _("TagAlong")

    user_type = models.CharField(
        max_length=1,
        choices=FamilyMemberTypes.choices,
        default=FamilyMemberTypes.ADULT
    )
    name = models.CharField(max_length=500)
    family_id = models.ForeignKey(Family, on_delete=models.DO_NOTHING)


class ActivityPartner(models.Model):
    """
    An organization hosting the extra-curricular event and learning experience. 
    The location/destination information for a CYM-sponsored activity
    The location stores the address for activity-partner or CYM location.
    """
    name = models.CharField(max_length=100)
    # todo - make this foreign key to a location entity?
    location = models.CharField(max_length=300)


class Dispatcher(models.Model):
    """coordinates pickup and return trips with family members, and drivers, and activity partner
        This person should be considered an administrator unless a different actor turns up that needs more specialized permissions
    """
    user_id = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)


class Event(models.Model):
    """Every event takes place at an activity partner's location
    """
    destination = models.ForeignKey(ActivityPartner, on_delete=models.CASCADE)
    event_date = models.DateTimeField(auto_now=True)
