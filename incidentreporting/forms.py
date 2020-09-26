from django.forms import ModelForm
from .models import incident
from django import forms
from django.contrib import messages


class Incident_Reporting_Form(ModelForm):
    class Meta:
        model = incident
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Incident_Reporting_Form, self).__init__(*args, **kwargs)

        SUB_INCIDENT_CHOICES = (
            ('ei', 'Environment Incident'),
            ('i', 'Injury/Illness'),
            ('pd', 'Property Damage'),
            ('v', 'Vehicle'),
        )
        self.fields['sub_incident_types'] = forms.MultipleChoiceField(choices = SUB_INCIDENT_CHOICES, widget=forms.CheckboxSelectMultiple())
