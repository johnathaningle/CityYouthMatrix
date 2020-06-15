from django.contrib import admin
from .models import (
    ActivityPartner,
    Event,
    Trip,
)


# class BookInline(admin.TabularInline):
#     model = Book

# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [
#         BookInline,
#     ]






admin.site.register(Trip)
admin.site.register(Event)
admin.site.register(ActivityPartner)
