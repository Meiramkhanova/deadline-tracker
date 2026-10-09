from django.urls import path

from .views import DeadlineListCreateView

urlpatterns = [
    path("deadlines/", DeadlineListCreateView.as_view(), name="deadline-list"),
]
