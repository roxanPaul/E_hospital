from django.urls import path
from . import views

urlpatterns = [


    path('home/',views.home,name='home'),
    path('update_doctor/<int:pk>/', views.doctor_profile_update, name='update_doctor'),
    path('delete_doctor/<int:pk>/', views.doctor_profile_delete, name='delete_doctor'),
    path('list_doctor/',views.doctor_profile_list,name='list_doctor'),
    path('add_doctor/',views.doctor_profile_add,name='add_doctor'),
    path('list_patient/',views.patient_list,name='list_patient'),
    path('update_patient/<int:pk>/',views.update_patient,name='update_patient'),
    path('delete_patient/<int:pk>/',views.delete_patient,name='delete_patient'),
    path('add_patient/',views.add_patient,name='add_patient'),

    path('facility_list/', views.facility_list, name='facility_list'),
    path('facility_detail/<int:pk>/', views.facility_detail, name='facility_detail'),
    path('facility_add/', views.facility_create, name='facility_add'),
    path('facility_update/<int:pk>/', views.facility_update, name='facility_update'),
    path('facility_delete/<int:pk>/', views.facility_delete, name='facility_delete'),

    path('appointments_list/', views.appointment_list, name='appointments_list'),
    path('appointments_detail/<int:pk>/', views.appointment_detail, name='appointments_detail'),
    path('appointments_create/', views.appointment_create, name='appointments_create'),
    path('appointments_update/<int:pk>/', views.appointment_update, name='appointments_update'),
    path('appointments_delete/<int:pk>/', views.appointment_delete, name='appointments_delete'),

    path('list_billing_statement/', views.list_billing_statements, name='list_billing_statement'),
    path('add_billing_statement', views.add_billing_statement, name='add_billing_statement'),
    path('update_billing_statement/<int:pk>/', views.update_billing_statement, name='update_billing_statement'),
    path('delete_billing_statement/<int:pk>/', views.delete_billing_statement, name='delete_billing_statement'),
]