from django.urls import path, include
from rest_framework.routers import SimpleRouter

from publisher.views import PublisherViewSet

router = SimpleRouter()
router.register("", PublisherViewSet)

urlpatterns = [
    path("", include(router.urls))
]
