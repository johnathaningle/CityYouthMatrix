from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import (
    Address,
    Driver,
    Family,
    FamilyAddress,
    FamilyMember,
    User,
)


class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'contact_number')
    fieldsets = (
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'contact_number')}),
        (None, {'fields': ('password',)}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    add_form = UserCreationForm


class DriverAdmin(admin.ModelAdmin):
    list_filter = ('is_verified',)

    def get_queryset(self, request):
        return super(DriverAdmin, self).get_queryset(request).select_related('user')

class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember


class FamilyAddressInline(admin.TabularInline):
    model = FamilyAddress


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('user', 'family_name', 'family_member_count')
    inlines = [
        FamilyMemberInline,
        FamilyAddressInline,
    ]

    def get_queryset(self, request):
        return super(FamilyAdmin, self).get_queryset(request).select_related('user')

    def family_name(self, obj):
        return obj.user.last_name

    def family_member_count(self, obj):
        return obj.familymember_set.count()


class FamilyAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'family', '__str__')

    def get_queryset(self, request):
        return super(FamilyAddressAdmin, self).get_queryset(request).select_related('family')

    def user(self, obj):
        return obj.family.user.email


admin.site.register(User, UserAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(FamilyAddress, FamilyAddressAdmin)
admin.site.register(FamilyMember)
