from django import forms
from .models import DoctorProfile,MedicalRecord

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['name', 'department','contact_number']
class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model= MedicalRecord

        fields = '__all__'