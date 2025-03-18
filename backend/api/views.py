from rest_framework import viewsets
from .models import Patient, MedicalData, Diagnosis
from .serializers import PatientSerializer, MedicalDataSerializer, DiagnosisSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class MedicalDataViewSet(viewsets.ModelViewSet):
    queryset = MedicalData.objects.all()
    serializer_class = MedicalDataSerializer

class DiagnosisViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
