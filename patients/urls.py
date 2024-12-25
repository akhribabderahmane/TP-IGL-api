from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DpiViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'dpi', DpiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]