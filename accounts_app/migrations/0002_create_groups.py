from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_groups(apps, schema_editor):
    # Create groups
    Group.objects.get_or_create(name='Patients')
    Group.objects.get_or_create(name='Doctors')
    Group.objects.get_or_create(name='Admins')

class Migration(migrations.Migration):
    dependencies = [
        ('accounts_app', '0001_initial'),  # Make sure this matches your initial migration
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]