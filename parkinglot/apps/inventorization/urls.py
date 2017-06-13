from django.conf.urls import url, include
from .views import InventorizationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'inventorization', InventorizationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
