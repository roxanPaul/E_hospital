# Generated by Django 4.2.11 on 2024-06-25 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0003_alter_billingstatement_appointment_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BillingStatement',
        ),
    ]
