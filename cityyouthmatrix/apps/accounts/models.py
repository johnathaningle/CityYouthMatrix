import uuid

from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Q
from django.http import QueryDict


def _get_random_username():
    return uuid.uuid4().hex[:30]


def random_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = _get_random_username()


class CustomUserManager(UserManager):
    def create_user(self, first_name, last_name, contact_number, email, password=None, **extra_fields):
        username = _get_random_username()
        extra_fields['first_name'] = first_name
        extra_fields['last_name'] = last_name
        extra_fields['contact_number'] = contact_number
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, first_name, last_name, contact_number, email, password=None, **extra_fields):
        username = _get_random_username()
        extra_fields['first_name'] = first_name
        extra_fields['last_name'] = last_name
        extra_fields['contact_number'] = contact_number
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    first_name = models.CharField(max_length=50, verbose_name='first name')
    last_name = models.CharField(max_length=150, verbose_name='last name')
    email = models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, unique=True, max_length=254, verbose_name='email address')
    contact_number = models.CharField(max_length=15)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'contact_number']

    def __str__(self):
        return self.email

models.signals.pre_save.connect(random_username, sender=User)


class Driver(models.Model):
    """Picks up or returns family and child(ren)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    car_make = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'




class Family(models.Model):

    class FamilyLanguages(models.TextChoices):
        ENGLISH = "EN", _("English")
        SPANISH = "ES", _("Spanish")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_language = models.CharField(
        max_length=2, choices=FamilyLanguages.choices)

    def __str__(self):
        return f'{self.user.last_name} Family'


class Address(models.Model):
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(blank=True, max_length=100)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.address_1}{' ' + self.address_2 if self.address_2 else ''} {self.city}, {self.state} {self.zip_code}"


class FamilyAddress(Address):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)


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
