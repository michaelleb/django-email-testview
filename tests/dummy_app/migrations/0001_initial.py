
from django.db import migrations

def create_admin_user(apps, schema_editor):
    """create admin user"""
    User = apps.get_model('auth', 'User')
    from django.contrib.auth.hashers import  make_password

    user = User(username='admin',
                email='admin@admin',
                password=make_password('admin'),
                is_staff=True,
                is_superuser=True)
    user.save()

def remove_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    qs = User.objects.filter(username='admin')
    if qs.exists():
        qs.delete()

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.RunPython(create_admin_user, remove_admin_user),
    ]
