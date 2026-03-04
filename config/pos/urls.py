from rest_framework.routers import DefaultRouter
from .views import POSViewSet

router = DefaultRouter()
router.register(r'', POSViewSet)

urlpatterns = router.urls