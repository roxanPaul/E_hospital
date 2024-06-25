from django.db import models
from django.contrib.auth.models import User

from doctor_app.models import DoctorProfile

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class FacilityManagement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    department = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    APPOINTMENT_STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('rescheduled', 'Rescheduled'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    doctor = models.ForeignKey('doctor_app.DoctorProfile', on_delete=models.CASCADE, related_name='admin_doctor_appointments')
    patient = models.ForeignKey('patient_app.Patient', on_delete=models.CASCADE, related_name='admin_patient_appointments')
    date_and_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS_CHOICES)

    def __str__(self):
        return f"{self.patient.name} - {self.date_and_time}"



class AdminProfile(models.Model):
    role=models.CharField(max_length=20)
    permission=models.CharField(max_length=50)


class BillingStatement(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    ]

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='billing_statements')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Billing Statement for {self.appointment.patient.name}"