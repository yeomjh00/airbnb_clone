from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# To control my custom models in admin page
# Belown(Decorator) is the same as : admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
