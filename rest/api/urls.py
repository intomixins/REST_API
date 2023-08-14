from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')


urlpatterns = router.urls
