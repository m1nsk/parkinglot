from django.conf.urls import url
from .views import AutoCardViewSet, CarModelViewSet, CarColorViewSet, CarOwnerViewSet, EntryViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'autocard', AutoCardViewSet)
router.register(r'model', CarModelViewSet)
router.register(r'color', CarColorViewSet)
router.register(r'owner', CarOwnerViewSet)
router.register(r'entry', EntryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]