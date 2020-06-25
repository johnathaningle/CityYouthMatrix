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
    list_display = ('email', 'first_name', 'last_name', 'contact_number', 'is_superuser')
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
    list_select_related = True

    def get_queryset(self, request):
        return super(DriverAdmin, self).get_queryset(request).select_related('user')

class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember


class FamilyAddressInline(admin.TabularInline):
    model = FamilyAddress


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('user', 'family_name', 'adults', 'children')
    list_select_related = True
    inlines = [
        FamilyMemberInline,
        FamilyAddressInline,
    ]

    def family_name(self, obj):
        return obj.user.last_name

    def adults(self, obj):
        return obj.familymember_set.filter(member_type='A').count()

    def children(self, obj):
        return obj.familymember_set.filter(member_type='C').count()


class FamilyAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'family', '__str__')
    list_select_related = True

    def user(self, obj):
        return obj.family.user.email


class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'family', 'full_name', 'member_type')
    list_filter = ('family', 'member_type',)
    list_select_related = True

    def user(self, obj):
        return obj.family.user.email


admin.site.register(User, UserAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(FamilyAddress, FamilyAddressAdmin)
admin.site.register(FamilyMember, FamilyMemberAdmin)
