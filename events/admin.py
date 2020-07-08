from django.contrib import admin
from django.conf import settings

from .models import Event, Tag, Location


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Admin config for EventTag model
    """

    list_display = ["name"]

    fields = ["name", "slug"]
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Admin config for Event model
    """

    list_display = getattr(
        settings,
        "EVENT_ADMIN_LIST_DISPLAY",
        ["title", "start_at", "end_at", "is_published"],
    )

    fieldsets = getattr(
        settings,
        "EVENT_ADMIN_FIELDSETS",
        (
            (
                "Details",
                {
                    "fields": [
                        "title",
                        "slug",
                        "intro",
                        "start_at",
                        "end_at",
                        "address",
                        "location",
                        "tags",
                    ]
                },
            ),
            ("Image", {"fields": ["photo"]}),
            ("Publishing", {"fields": ["is_published", "publish_at"]}),
            ("Metadata", {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},),
        ),
    )

    readonly_fields = getattr(
        settings, "EVENT_ADMIN_READONLY_FIELDS", ["created_at", "updated_at"]
    )
    prepopulated_fields = {"slug": ["title"]}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """
    Admin class for the location model
    """

    list_display = ["name", "lat", "lng"]
    readonly_fields = ["created_at", "updated_at"]
    fieldsets = [
        (None, {"fields": ["name", "lat", "lng"]}),
        (
            "Meta Data",
            {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},
        ),
    ]
