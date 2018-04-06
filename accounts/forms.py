from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length ='20')
    last_name = forms.CharField(max_length = '20')
    email = forms.EmailField(required = True)
    college = forms.CharField(max_length=100)
    contact = forms.IntegerField()
    profile_pic = forms.ImageField()

    class Meta:
        model = Student
        fields =(
            #'username',
            'first_name',
            'last_name',
            'profile_pic',
            'email',
            'contact',
            'college',
            'password1',
            'password2'
        )


class TeacherRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length ='20')
    last_name = forms.CharField(max_length = '20')
    email = forms.EmailField(required = True)
    qualifications = forms.TextField(max_length=100)
    contact = forms.IntegerField()
    profile_pic = forms.ImageField()

    class Meta:
        model = Teacher
        fields =(
           # 'username',
            'first_name',
            'last_name',
            'profile_pic',
            'email',
            'contact',
            'qualifications',
            'password1',
            'password2'
        )