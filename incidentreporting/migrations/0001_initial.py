# Generated by Django 3.0.7 on 2020-09-26 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('ch', 'Corporate Headoffice')], default='ch', max_length=6)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('incident_location', models.CharField(max_length=100)),
                ('initial_severity', models.CharField(choices=[('l', 'Low'), ('m', 'Moderate'), ('h', 'High'), ('e', 'Extreme')], default='m', max_length=1)),
                ('suspected_cause', models.TextField()),
                ('immediate_action_taken', models.TextField()),
                ('sub_incident_types', models.CharField(max_length=3)),
                ('incident_reporter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]