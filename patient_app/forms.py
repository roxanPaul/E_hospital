from django import forms
from .models import MedicalRecord, Appointment,Patient

class PatientRegistrationForm(forms.ModelForm):
    # You may include additional fields as needed for patient registration
    class Meta:
        model = Patient
        fields = '__all__'
        # Add more fields as needed

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnoses', 'medications', 'allergies', 'treatment_history']
        widgets = {
            'diagnoses': forms.Textarea(attrs={'rows': 4}),
            'medications': forms.Textarea(attrs={'rows': 4}),
            'allergies': forms.Textarea(attrs={'rows': 4}),
            'treatment_history': forms.Textarea(attrs={'rows': 4}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date_and_time']

class SearchForm(forms.Form):
    patient_name = forms.CharField(label='Patient Name', max_length=100)