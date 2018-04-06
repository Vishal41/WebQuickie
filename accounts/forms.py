from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class StudentRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget = forms.PasswordInput())
  password2 = forms.CharField(widget=forms.PasswordInput())

  class Meta:
      model = User
      fields =[
          'username',
          'email',
          'password',
      ]


class TeacherRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget = forms.PasswordInput())
  password2 = forms.CharField(widget=forms.PasswordInput())

  class Meta:
      model = User
      fields =[
          'username',
          'email',
          'password',
      ]