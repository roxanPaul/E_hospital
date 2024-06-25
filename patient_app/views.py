from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MedicalRecord, HealthResource,Patient
from head_app.models import FacilityManagement,Appointment,BillingStatement
from doctor_app.models import DoctorProfile
from .forms import PatientRegistrationForm, MedicalRecordForm, AppointmentForm,SearchForm
from accounts_app.models import CustomUser
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
import stripe

def home(request):
    return render(request, 'base.html')


def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def facility_page(request):
    facilities = FacilityManagement.objects.all()
    print(facilities)
    return render(request, 'patient/facility_page.html', {'facilities': facilities})

def doc_list(request):
    doctors = DoctorProfile.objects.all()
    return render(request,'patient/doc_list.html',{'doctors':doctors})


def Patient_profile(request):
    try:
        patient_profile = Patient.objects.get(id=request.user.id)  # Assuming you have some unique identifier like id
    except Patient.DoesNotExist:
        patient_profile = None

    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST, instance=patient_profile)
        if form.is_valid():
            patient_profile = form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('appointment_booking')  # Replace 'base' with your actual redirect URL
    else:
        form = PatientRegistrationForm(instance=patient_profile)

    context = {
        'form': form,
    }
    return render(request, 'patient/profile.html', context)

@login_required
def display_profile(request):
    patient_profile = get_object_or_404(Patient, user=request.user)
    medical_records = MedicalRecord.objects.filter(patient=request.user)

    context = {
        'patient_profile': patient_profile,
        'medical_records': medical_records
    }
    return render(request, 'patient/display_profile.html', context)


def search_view(request):
    form = SearchForm(request.POST or None)
    results = None
    if request.method == 'POST' and form.is_valid():
        query = form.cleaned_data.get('query')
        if query:
            results = Patient.objects.filter(user__username__icontains=query)
    context = {
        'form': form,
        'results': results,
    }
    return render(request, 'patient/search_results.html', context)
@login_required
def appointment_booking(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment created successfully.')
            return redirect('appointment_booking')
    else:
        form = AppointmentForm()
    return render(request, 'patient/appointment_booking.html', {'form': form})

@login_required
def complete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = 'completed'
    appointment.save()

    # Create or update the billing statement
    billing, created = BillingStatement.objects.get_or_create(appointment=appointment)
    if created:
        billing.amount_due = 100.00  # Set the appropriate amount
        billing.due_date = timezone.now() + timezone.timedelta(days=30)
        billing.save()

    return redirect('view_billing', billing_id=billing.id)

def success(request):
    return render(request, 'patient/success.html')
def cancel(request):
    return render(request,'patient/cancel.html')
@login_required
def health_resources(request):
    resources = HealthResource.objects.all()
    return render(request, 'patient/health_resources.html', {'resources':resources})


@login_required
def view_billing(request, billing_id):
    billing = get_object_or_404(BillingStatement, id=billing_id)
    return render(request, 'patient/billing_statement.html', {'billing': billing})

@login_required
def patient_billing_statements(request):
    try:
        user = request.user  # Assuming the user is logged in with CustomUser
        patients = user.patients.all()

        billing_statements = BillingStatement.objects.filter(appointment__patient__in=patients)

    except CustomUser.DoesNotExist:
        billing_statements = []

    return render(request, 'patient/patient_billing_statements.html', {'billing_statements': billing_statements})
@login_required
def payment_billing_session(request, id):
    try:
        bill = BillingStatement.objects.get(id=id, appointment__patient=request.user.patient)
    except BillingStatement.DoesNotExist:
        return redirect('patient_billing_statements')

    amount_due = bill.amount_due

    line_item = {
        'price_data': {
            'currency': 'INR',
            'unit_amount': int(amount_due * 100),
            'product_data': {
                'name': f'Billing Statement #{bill.id}',
            },
        },
        'quantity': 1,
    }

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[line_item],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('payment_success')),  # Adjust success and cancel URLs
        cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
    )

    return redirect(checkout_session.url, code=303)

def medical_record_display(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medical record saved successfully.')
            return redirect('medical_record_display')
    else:
        form = MedicalRecordForm()

    records = MedicalRecord.objects.all()

    context = {
        'form': form,
        'records': records,
    }
    return render(request, 'patient/medical_record_display.html', context)


def patient_add(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_booking')  # Redirect to doctor profiles or any desired page
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient/patient_add.html', {'form': form})