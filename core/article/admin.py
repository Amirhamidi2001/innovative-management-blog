from django.contrib import admin
from article.models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Contact model.
    """

    date_hierarchy = "created_date"
    list_display = ("name", "email")
    list_filter = ("email",)
    search_fields = ("name", "message")


admin.site.register(Contact, ContactAdmin)
