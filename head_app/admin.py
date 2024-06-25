from django.contrib import admin
from .models import  FacilityManagement,Appointment,BillingStatement


admin.site.register(FacilityManagement)
admin.site.register(Appointment)
admin.site.register(BillingStatement)

