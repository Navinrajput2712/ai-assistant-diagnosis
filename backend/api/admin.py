from django.contrib import admin
from .models import Patient, MedicalData, Diagnosis

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "mobile", "created_at")
    search_fields = ("name", "mobile")
    list_filter = ("created_at", "gender")

@admin.register(MedicalData)
class MedicalDataAdmin(admin.ModelAdmin):
    list_display = ("patient", "blood_pressure", "temperature", "diabetes_status")
    list_filter = ("diabetes_status",)

@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ("patient", "diagnosis", "treatment_plan", "created_at")
    search_fields = ("diagnosis",)
