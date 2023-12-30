from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from main.models import *



@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ( 'phone_number', 'region')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(Region)
admin.site.register(Restoran)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(Reservetion_table)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Service)
admin.site.register(Achievement)
admin.site.register(Language)
admin.site.register(Git)
admin.site.register(Order_room)
admin.site.register(Employee)
