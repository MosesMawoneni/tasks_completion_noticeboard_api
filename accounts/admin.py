from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm,CustomUserCreationForm


# The class `CustomUserAdmin` extends `UserAdmin` and customizes the admin interface for the
# `CustomUser` model.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = (
        "email",
        "name",
        "is_staff",
        "username"
    )
    fieldsets = UserAdmin.fieldsets + ((None,{"fields":("name","date_engaged","date_of_birth","role")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{"fields":("name","date_engaged","date_of_birth","role")}),)

admin.site.register(CustomUser,CustomUserAdmin)
