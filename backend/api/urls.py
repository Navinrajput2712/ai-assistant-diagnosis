from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, MedicalDataViewSet, DiagnosisViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'medical', MedicalDataViewSet)
router.register(r'diagnosis', DiagnosisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
