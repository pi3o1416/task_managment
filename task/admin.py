from django.contrib import admin

from .models import Task, TaskAssignment, TaskSubmission
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('headline', 'created_by', 'created_at', 'last_date',)
    list_filter = ("created_at", "created_by", "last_date",)
    search_fields = ("headline", "created_by",)

@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ('task', 'assigned_to', 'assighed_at', 'is_submitted', 'notified',)
    list_filter = ("is_submitted", "assigned_to", "assighed_at",)
    search_fields = ("task",)


@admin.register(TaskSubmission)
class TaskSubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'submission_date',)
    list_filter = ("assignment", "submission_date",)





