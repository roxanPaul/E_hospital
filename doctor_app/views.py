from django.shortcuts import render,redirect
from .models import DoctorProfile,  MedicalRecord
from django.shortcuts import render, get_object_or_404
from .forms import DoctorProfileForm,MedicalRecordForm
from django.contrib import messages
from head_app.models import Appointment


def home(request):
    return render(request,'doctor/patient_dashboard.html')
def create_doctor_profile(request):
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST)
        if form.is_valid():
            doctor_profile = form.save()
            return redirect('doctor_list')
    else:
        form = DoctorProfileForm()

    return render(request, 'doctor/profile.html', {'form': form})

def doctor_list(request):
    doctors = DoctorProfile.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})

def appointment_schedule(request, doctor_id):
    doctor = get_object_or_404(DoctorProfile, id=doctor_id)
    appointments = Appointment.objects.filter(doctor=doctor)
    context = {
        'doctor': doctor,
        'appointments': appointments,
    }
    return render(request, 'doctor/appointment_schedule.html', context)


def medical_record_list(request):
    records = MedicalRecord.objects.all()
    return render(request, 'doctor/record_list.html', {'records': records})

def medical_record_detail(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    return render(request, 'doctor/record_detail.html', {'record': record})


def medical_record_create(request, patient_id):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.patient_id = patient_id  # Assign patient_id from URL
            medical_record.save()
            return redirect('record_list')  # Redirect to record list view
    else:
        form = MedicalRecordForm()
    return render(request, 'doctor/record_add.html', {'form': form})

def medical_record_update(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            return redirect('record_list')  # Redirect to record list view
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'doctor/record_update.html', {'form': form})

def medical_record_delete(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        medical_record.delete()
        return redirect('record_list')
    return render(request, 'doctor/record_delete.html', {'medical_record': medical_record})