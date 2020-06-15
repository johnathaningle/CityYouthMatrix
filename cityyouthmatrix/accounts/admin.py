from django.contrib import admin
from .models import (
    Address,
    Driver,
    Family,
    FamilyAddress,
    FamilyMember,
    User,
)

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Driver)
admin.site.register(Family)
admin.site.register(FamilyAddress)
admin.site.register(FamilyMember)
