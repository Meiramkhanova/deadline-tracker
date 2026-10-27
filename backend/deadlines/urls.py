from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DeadlineViewSet

router = DefaultRouter()
router.register("deadlines", DeadlineViewSet, basename="deadline")

urlpatterns = [
    path("", include(router.urls)),
]
