from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name = 'Dashboard'),
    path('incident/reporting/', views.incidentreporting, name = 'Incident-Reporting'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
