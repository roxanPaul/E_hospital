
from django.db import models
from django.contrib.auth.models import User




class DoctorProfile(models.Model):

    name=models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)



    def __str__(self):
        return self.name




class MedicalRecord(models.Model):
    patient = models.ForeignKey('patient_app.Patient', on_delete=models.CASCADE, related_name='medical_records')
    diagnoses = models.TextField()
    medications = models.TextField()
    treatment_plan = models.TextField()

    def __str__(self):
        return f"Medical record for {self.patient.name}"
