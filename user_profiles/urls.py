from django.urls import include, path
from rest_framework import routers
from .views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r"", ProfileViewSet)

# wire up API
urlpatterns = [path("", include(router.urls))]
