from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    height = models.FloatField()
    weight = models.FloatField()
    gender = models.CharField(max_length=10)
    symptoms = models.TextField()
    medical_history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MedicalData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    blood_pressure = models.CharField(max_length=50)
    temperature = models.FloatField()
    diabetes_status = models.CharField(max_length=20)

class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
