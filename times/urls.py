from rest_framework import routers
from .views import CaracteristicaViewSet, TimeViewSet


router = routers.DefaultRouter()
router.register(r'time', TimeViewSet)
router.register(r'caracteristica', CaracteristicaViewSet)
urlpatterns = router.urls