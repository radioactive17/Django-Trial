from django.db import models
from django.contrib.auth.models import User

class incident(models.Model):
    incident_reporter = models.OneToOneField(User, on_delete = models.CASCADE)
    #incident detials
    LOCATION_CHOICES = (
        ('ch', 'Corporate Headoffice'),
    )
    location = models.CharField(max_length = 6, choices = LOCATION_CHOICES, default = 'ch')
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    incident_location = models.CharField(max_length = 100)

    SEVERITY_CHOICES = (
        ('l', 'Low'),
        ('m', 'Moderate'),
        ('h', 'High'),
        ('e', 'Extreme'),
    )
    initial_severity = models.CharField(max_length = 1, choices = SEVERITY_CHOICES, default = 'm')
    suspected_cause = models.TextField()
    immediate_action_taken = models.TextField()

    sub_incident_types = models.CharField(max_length = 3)
