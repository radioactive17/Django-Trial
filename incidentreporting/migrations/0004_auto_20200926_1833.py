# Generated by Django 3.0.7 on 2020-09-26 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('incidentreporting', '0003_auto_20200926_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='incident_reporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
