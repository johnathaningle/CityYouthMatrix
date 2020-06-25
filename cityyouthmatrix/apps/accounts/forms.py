from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
