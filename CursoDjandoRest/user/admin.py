from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as Admin
from user.models import User


@admin.register(User)
class UserAdmin(Admin):
    """ fieldsets = (
         (None, {'fields': ('username', 'password')}),
         ('Informacion Personal', {'fields': ('first_name', 'last_name', 'email')})
     )"""
    pass
