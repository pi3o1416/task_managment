from django.contrib import admin
from .models import Notification

# Register your models here.


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['notification_headline', 'notification_to',]
    list_filter = ['notification_to', 'notification_at',]
    search_fields = ['notification_headline', 'description',]

