from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Q


class User(AbstractUser):
    contact_number = models.CharField(max_length=15)


class Driver(models.Model):
    """Picks up or returns family and child(ren)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=9)


class Family(models.Model):

    class FamilyLanguages(models.TextChoices):
        ENGLISH = "EN", _("English")
        SPANISH = "ES", _("Spanish")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_language = models.CharField(
        max_length=2, choices=FamilyLanguages.choices)


class Address(models.Model):
    address_1 = models.CharField(max_length=300)
    address_2 = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)


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
