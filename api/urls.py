
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, LocationViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'locations', LocationViewSet, basename='location')

urlpatterns = [
    path('api/', include(router.urls)),
]
