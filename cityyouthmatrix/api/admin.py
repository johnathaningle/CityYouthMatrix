from django.contrib import admin
from .models import (
    ActivityPartner,
    Driver,
    Event,
    Family,
    FamilyAddress,
    FamilyMember,
    Trip,
)


# class BookInline(admin.TabularInline):
#     model = Book

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [
#         BookInline,
#     ]





admin.site.register(Driver)
admin.site.register(Trip)
admin.site.register(Family)
admin.site.register(FamilyMember)
admin.site.register(ActivityPartner)
