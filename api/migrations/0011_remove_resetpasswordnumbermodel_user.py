# Generated by Django 4.2.4 on 2023-09-12 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_profilemodel_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resetpasswordnumbermodel',
            name='user',
        ),
    ]
