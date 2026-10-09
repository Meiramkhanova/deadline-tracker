from django.contrib import admin

from .models import Deadline


@admin.register(Deadline)
class DeadlineAdmin(admin.ModelAdmin):
    list_display = ["title", "subject", "due_at", "is_done"]
    list_filter = ["is_done", "subject"]
