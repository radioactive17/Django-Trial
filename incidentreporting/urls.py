from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('incident-reporting/form', views.incidentreporting_form, name = 'Incident-Reporting-Form'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
