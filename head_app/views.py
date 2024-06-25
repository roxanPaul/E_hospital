from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import  DoctorProfileForm, PatientProfileForm,AppointmentManagementForm,FacilityForm,BillingStatementForm
from django.apps import apps
from . models import FacilityManagement,Appointment,BillingStatement
from django.contrib.auth import authenticate, login


from patient_app.models import Patient

from doctor_app.models import DoctorProfile




def home(request):
    return render(request,'head/head_dashboard.html')

#Doctor Section

def doctor_profile_update(request, pk):
    doctor = get_object_or_404(DoctorProfile, pk=pk)
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('list_doctor')  # Replace with your URL name for doctor profile list
    else:
        form = DoctorProfileForm(instance=doctor)
    return render(request, 'head/update_doctor_profile.html', {'form': form})

def doctor_profile_delete(request, pk):
    doctor = get_object_or_404(DoctorProfile, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('list_doctor')  # Replace with your URL name for doctor profile list
    return render(request, 'head/delete_doctor_profile.html', {'doctor': doctor})


def doctor_profile_list(request):
    doctors = DoctorProfile.objects.all()
    return render(request, 'head/list_doctor_profile.html', {'doctors': doctors})


def doctor_profile_add(request):
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_doctor')
    else:
        form = DoctorProfileForm()

    return render(request, 'head/add_doctor_profile.html', {'form': form})


#Patient Section
def add_patient(request):
    if request.method == 'POST':
        form = PatientProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_patient')  # Redirect to doctor profiles or any desired page
    else:
        form = PatientProfileForm()
    return render(request, 'head/add_patient.html', {'form': form})

def update_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('list_patient')  # Redirect to doctor profiles or any desired page
    else:
        form = PatientProfileForm(instance=patient)
    return render(request, 'head/update_patient.html', {'form': form})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('list_patient')  # Redirect to doctor profiles or any desired page
    return render(request, 'head/delete_patient.html', {'patient': patient})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'head/patient_list.html', {'patients': patients})
#Facility Section
def facility_list(request):
    facilities = FacilityManagement.objects.all()
    return render(request, 'head/facility_list.html', {'facilities': facilities})


def facility_detail(request, pk):
    facility = get_object_or_404(FacilityManagement, pk=pk)
    return render(request, 'head/facility_detail.html', {'facility': facility})


def facility_create(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Facility created successfully.')
            return redirect('facility_list')
    else:
        form = FacilityForm()
    return render(request, 'head/facility_add.html', {'form': form})


def facility_update(request, pk):
    facility = get_object_or_404(FacilityManagement, pk=pk)
    if request.method == 'POST':
        form = FacilityForm(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            messages.success(request, 'Facility updated successfully.')
            return redirect('facility_list')
    else:
        form = FacilityForm(instance=facility)
    return render(request, 'head/facility_update.html', {'form': form})


def facility_delete(request, pk):
    facility = get_object_or_404(FacilityManagement, pk=pk)
    if request.method == 'POST':
        facility.delete()
        messages.success(request, 'Facility deleted successfully.')
        return redirect('facility_list')
    return render(request, 'head/facility_confirm_delete.html', {'facility': facility})

#Appointment Section
def appointment_list(request):
    appointments = Appointment.objects.all()


    return render(request, 'head/appointment_list.html', {'appointments': appointments})

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'head/appointment_detail.html', {'appointment': appointment})

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentManagementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment created successfully.')
            return redirect('appointments_list')
    else:
        form = AppointmentManagementForm()
    return render(request, 'head/appointment_create.html', {'form': form})


def appointment_update(request, pk):
    Appointment = apps.get_model('doctor_app', 'Appointment')
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == 'POST':
        form = AppointmentManagementForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully.')
            return redirect('appointment_list')
    else:
        form = AppointmentManagementForm(instance=appointment)

    return render(request, 'head/appointment_form.html', {'form': form})
def appointment_delete(request, pk):
    Appointment = apps.get_model('doctor_app', 'Appointment')
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully.')
        return redirect('appointment_list')
    return render(request, 'head/appointment_confirm_delete.html', {'appointment': appointment})


#Billing Section


def add_billing_statement(request):
    if request.method == 'POST':
        form = BillingStatementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Billing statement added successfully.')
            return redirect('list_billing_statement')
    else:
        form = BillingStatementForm()
    return render(request, 'head/add_billing_statement.html', {'form': form})

def update_billing_statement(request, pk):
    billing_statement = get_object_or_404(BillingStatement, pk=pk)
    if request.method == 'POST':
        form = BillingStatementForm(request.POST, instance=billing_statement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Billing statement updated successfully.')
            return redirect('list_billing_statement')
    else:
        form = BillingStatementForm(instance=billing_statement)
    return render(request, 'head/update_billing_statement.html', {'form': form})

def delete_billing_statement(request, pk):
    billing_statement = get_object_or_404(BillingStatement, pk=pk)
    if request.method == 'POST':
        billing_statement.delete()
        messages.success(request, 'Billing statement deleted successfully.')
        return redirect('list_billing_statement')
    return render(request, 'head/delete_billing_statement.html', {'billing_statement': billing_statement})

def list_billing_statements(request):
    billing_statements = BillingStatement.objects.all()
    return render(request, 'head/list_billing_statement.html', {'billing_statements': billing_statements})