# Generated by Django 4.2.4 on 2023-09-09 12:17

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_alter_profilemodel_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', related_query_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ResetPasswordNumberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254)),
                ('number', models.CharField(blank=True, default=api.models.create_number, max_length=6)),
                ('attempt', models.IntegerField(blank=True, default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resetpasswordnumbers', related_query_name='resetpasswordnumber', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
