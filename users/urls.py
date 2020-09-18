from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.user_login, name = 'Login'),
    path('logout/',views.user_logout, name = 'Logout'),
    path('register/', views.register, name = 'SignUp'),
    path('profile/', views.profile, name = 'Profile'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
