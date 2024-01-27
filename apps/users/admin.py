from django.contrib import admin
from unfold.admin import ModelAdmin
from users.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = (
        "email",
        "username",
        "full_name",
        "is_active",
        "is_staff",
        "is_deleted",
    )
    list_filter = (
        "is_active",
        "is_staff",
    )
    fields = (
        "first_name",
        "last_name",
        "email",
        "username",
        "is_active",
        "is_staff",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "username",
        "id",
    )

    list_filter_submit = True
