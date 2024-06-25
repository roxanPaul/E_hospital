from django.urls import path
from . import views

urlpatterns = [
    path('doctor_profile/',views.create_doctor_profile,name='doctor_profile'),
    path('appointment/<int:id>/',views.appointment_schedule,name='appointment'),
    path('doctor_list/',views.doctor_list,name='doctor_list'),
    path('record_list/',views.medical_record_list,name='record_list'),
    path('record_detail/<int:pk>',views.medical_record_detail,name='record_detail'),
    path('record_update/<int:pk>/',views.medical_record_update,name='record_update'),
    path('record_add/',views.medical_record_create,name='record_add'),
    path('record_delete/<int:pk>/',views.medical_record_delete,name='record_delete'),
    path('homes/',views.home,name='homes'),
]
