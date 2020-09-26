from django.forms import ModelForm
from .models import incident
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import EndUser
from django.forms.widgets import DateInput, TimeInput

class Incident_Reporting_Form(ModelForm):
    class Meta:
        model = incident
        exclude = ['incident_reporter']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, user,  *args, **kwargs):
        super(Incident_Reporting_Form, self).__init__(*args, **kwargs)
        SUB_INCIDENT_CHOICES = (
            ('ei', 'Environment Incident'),
            ('i', 'Injury/Illness'),
            ('pd', 'Property Damage'),
            ('v', 'Vehicle'),
        )
        self.fields['sub_incident_types'] = forms.MultipleChoiceField(choices = SUB_INCIDENT_CHOICES, widget=forms.CheckboxSelectMultiple())
