from django import forms
from django.contrib.auth.models import User
from doctor_app.models import DoctorProfile
from patient_app.models import Patient
from .models import Appointment,FacilityManagement

from .models import BillingStatement

class BillingStatementForm(forms.ModelForm):
    class Meta:
        model = BillingStatement
        fields = ['appointment', 'amount_due', 'due_date', 'payment_status']


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [ 'name','date_of_birth','age', 'address', 'phone_number']

class AppointmentManagementForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'



class FacilityForm(forms.ModelForm):
    class Meta:
        model = FacilityManagement
        fields = '__all__'




class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['name', 'department', 'contact_number']