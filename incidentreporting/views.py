from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import incident
from .forms import Incident_Reporting_Form
from django.urls import reverse

@login_required
def incidentreporting_form(request):
    if request.method == 'POST':
        form = Incident_Reporting_Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Incident_Reporting_Form()
    return render(request, 'incidentreporting/incidentreporting_form.html', {'form':form})
