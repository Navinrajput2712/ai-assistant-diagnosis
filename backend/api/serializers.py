from rest_framework import serializers
from .models import Patient, MedicalData, Diagnosis

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'mobile', 'address', 'height', 'weight', 'gender', 'symptoms', 'medical_history', 'created_at']

class MedicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalData
        fields = ['id', 'patient', 'blood_pressure', 'temperature', 'diabetes_status']

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['id', 'patient', 'diagnosis', 'treatment_plan', 'created_at']