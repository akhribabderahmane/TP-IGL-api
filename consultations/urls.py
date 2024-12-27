from rest_framework.routers import DefaultRouter
from .views import DpiViewSet, ConsultationViewSet, OrdonnanceViewSet, MedicamentViewSet

router = DefaultRouter()
router.register(r'dpis', DpiViewSet)
router.register(r'consultations', ConsultationViewSet)
router.register(r'ordonnances', OrdonnanceViewSet)
router.register(r'medicaments', MedicamentViewSet)

urlpatterns = router.urls
