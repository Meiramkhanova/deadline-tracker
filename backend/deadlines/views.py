from rest_framework import generics

from .models import Deadline
from .serializers import DeadlineSerializer


class DeadlineListCreateView(generics.ListCreateAPIView):
    queryset = Deadline.objects.all()
    serializer_class = DeadlineSerializer
