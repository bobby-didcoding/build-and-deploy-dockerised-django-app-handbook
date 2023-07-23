# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("email", "first_name", "last_name", "is_active", "is_staff")
    ordering = ("-created",)
    list_display = ("email", "first_name", "last_name", "is_active", "is_staff")

    fieldsets = (
        (None, {"fields": ("email", "first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
