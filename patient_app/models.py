
from django.db import models
from django.contrib.auth.models import User
from doctor_app.models import DoctorProfile
from head_app.models import Appointment

class Patient(models.Model):

    name=models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    age=models.IntegerField()
    def __str__(self):
        return self.name







class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_medical_records')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctors_record')
    diagnoses = models.TextField()
    medications = models.TextField()
    allergies = models.TextField()
    treatment_history = models.TextField()


    def __str__(self):
        return self.patient.name + "'s Medical Record"



class HealthResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)


    def __str__(self):
        return self.title



