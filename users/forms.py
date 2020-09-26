from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import EndUser
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'username', 'email', 'password1', 'password2', 'image']

    def clean(self):
        try:
            if EndUser.objects.get(email = self.cleaned_data['email']):
                raise forms.ValidationError('User already exists')
        except EndUser.DoesNotExist:
            pass
        try:
            if User.objects.get(username = self.cleaned_data['username']):
                raise forms.ValidationError('username taken')
        except User.DoesNotExist:
            pass
        return self.cleaned_data
