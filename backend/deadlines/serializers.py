from django.utils import timezone
from rest_framework import serializers

from .models import Deadline


class DeadlineSerializer(serializers.ModelSerializer):
    days_left = serializers.SerializerMethodField()

    class Meta:
        model = Deadline
        fields = ["id", "title", "subject", "due_at", "is_done", "days_left", "created_at"]
        read_only_fields = ["id", "created_at"]

    def get_days_left(self, obj):
        return (obj.due_at - timezone.now()).days
