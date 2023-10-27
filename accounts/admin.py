from django.contrib import admin
from .models import CustomeUser,Profile
from django.contrib.auth.admin import UserAdmin

class CustomeUserAdmin(UserAdmin):
    list_display = ('email','is_staff','is_active','is_superuser','is_verified')
    list_filter = ('is_verified',)
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        ('Basic data', {'fields': ('email','username','password')}),
        ('Permissions', {'fields': ('is_staff','is_active','is_superuser','is_verified','groups','user_permissions')}),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',),'fields': ('email', 'username', 'password1', 'password2')}),)

class CostumeProfile(UserAdmin):
    list_display = ('user','first_name','last_name')
    list_filter = ('first_name','last_name',)
    filter_horizontal = ()
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name','last_name', )
    fieldsets= (('User Profile', {'fields':('image', 'first_name', 'last_name', 'phone', 'address')}),)
    add_fieldsets =(
        None, {'calsses':('wide',),'fields':('first_name', 'last_name', 'phone')}
    )




admin.site.register(CustomeUser, CustomeUserAdmin)
admin.site.register(Profile,CostumeProfile)