from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models

class Driver(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)

class DriverNote(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=500)

class Trip(models.Model):

    pickup_location = models.CharField(max_length=300) #todo - make this foreign key to a location entity?
    pickup_completed = models.BooleanField(default=False)
    pickup_driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, related_name="PickupDriver")

    return_location = models.CharField(max_length=300) #todo - make this foreign key to a location entity?
    return_complted = models.BooleanField(default=False)
    return_driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, related_name="ReturnDriver")

class Family(models.Model):
    description = models.CharField(max_length=300, null=True)

class FamilyMember(models.Model):

    class FamilyMemberTypes(models.TextChoices):
        CHILD = "C", _("Child")
        ADULT = "A", _("Adult")
        TAG_ALONG = "T", _("TagAlong")

    user_type = models.CharField(
        max_length=1,
        choices= FamilyMemberTypes.choices,
        default=FamilyMemberTypes.ADULT
    )
    name = models.CharField(max_length=500)
    family_id = models.ForeignKey(Family, on_delete=models.DO_NOTHING)



class ActivityPartner(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=300) #todo - make this foreign key to a location entity?

class Dispatcher(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)