from rest_framework import viewsets

from .models import Deadline
from .serializers import DeadlineSerializer


class DeadlineViewSet(viewsets.ModelViewSet):
    """Full CRUD for deadlines: list, retrieve, create, update, delete."""

    queryset = Deadline.objects.all()
    serializer_class = DeadlineSerializer
