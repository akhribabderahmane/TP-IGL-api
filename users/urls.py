from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, UserViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
