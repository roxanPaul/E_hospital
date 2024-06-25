from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('registers/', views.register, name='registers'),
    path('head_dashboard/', views.head_dashboard, name='head_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard', views.patient_dashboard, name='patient_dashboard'),
]