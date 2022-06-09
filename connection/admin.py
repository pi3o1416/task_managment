from django.contrib import admin
from .models import Connection

# Register your models here.


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ("connected_from", "connected_to", "connection_status", "connected_at")
    list_filter = ("connected_from", "connected_to", "connection_status", "connected_at")
    search_fields = ("connected_from", "connected_to", "connection_status")
