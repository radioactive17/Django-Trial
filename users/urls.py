from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.user_login, name = 'Login'),
    path('register/', views.register, name = 'SignUp'),
    path('profile/', views.profile, name = 'Profile'),
]
