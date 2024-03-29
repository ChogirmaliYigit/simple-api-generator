from applications.models import Application, ApplicationConfig
from django.contrib import admin
from unfold.admin import ModelAdmin


@admin.register(Application)
class ApplicationAdmin(ModelAdmin):
    list_display = (
        "title",
        "description",
        "owner",
        "visibility",
        "uuid",
        "is_deleted",
    )
    list_filter = ("visibility",)
    fields = (
        "title",
        "description",
        "owner",
        "visibility",
    )
    search_fields = (
        "owner__first_name",
        "owner__last_name",
        "owner__username",
        "owner__email",
        "id",
        "uuid",
    )

    list_filter_submit = True


@admin.register(ApplicationConfig)
class ApplicationConfigAdmin(ModelAdmin):
    list_display = (
        "application",
        "page_size",
    )
    fields = (
        "application",
        "page_size",
    )
    search_fields = (
        "application__title",
        "application__description",
        "application__uuid",
        "page_size",
        "id",
    )

    list_filter_submit = True
