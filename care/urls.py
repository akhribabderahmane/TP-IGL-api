from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SoinViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'soins', SoinViewSet, basename='soin')

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
