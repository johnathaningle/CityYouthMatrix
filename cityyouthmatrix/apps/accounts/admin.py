from django import forms
from django.contrib import admin
from .models import (
    Address,
    Driver,
    Family,
    FamilyAddress,
    FamilyMember,
    User,
)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'contact_number')
    readonly_fields = ()
    exclude = ('user_permissions', 'groups', 'username')


class DriverAdmin(admin.ModelAdmin):

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



admin.site.register(User, UserAdmin)
admin.site.register(Address)
admin.site.register(Driver)
admin.site.register(Family, FamilyAdmin)
admin.site.register(FamilyAddress)
admin.site.register(FamilyMember)
