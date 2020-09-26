from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import incident
from .forms import Incident_Reporting_Form
from django.urls import reverse

@login_required
def dashboard(request):
    return render(request, 'incidentreporting/base.html')


@login_required
def incidentreporting(request):
    if request.method == 'POST':
        form = Incident_Reporting_Form(data = request.POST, user = request.user)
        if form.is_valid():
            user = request.user
            i = incident(incident_reporter = user, location = form.cleaned_data['location'], description = form.cleaned_data['description'],
                        date = form.cleaned_data['date'], time = form.cleaned_data['time'], incident_location = form.cleaned_data['incident_location'],
                        initial_severity = form.cleaned_data['initial_severity'], suspected_cause = form.cleaned_data['suspected_cause'],
                        immediate_action_taken = form.cleaned_data['immediate_action_taken'], sub_incident_types = form.cleaned_data['sub_incident_types'])
            i.save()
            messages.success(request, f"Incident Reported Successfully!")
            return redirect('Dashboard')
    else:
        form = Incident_Reporting_Form(request.user)
    return render(request, 'incidentreporting/incidentreporting_form.html', {'form':form})
