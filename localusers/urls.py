from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    GroupViewSet,
)

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = router.urls
