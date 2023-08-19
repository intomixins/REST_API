from rest_framework import routers
from .views import UserAPIView

router = routers.DefaultRouter()
router.register('api/users', UserAPIView, 'users')


urlpatterns = router.urls
