from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login, authenticate

def RegistrationStudent(request):
    if request.method == 'POST':
        form = StudenRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/home/')

    else:
        form = StudentRegistrationForm
        context = {'form' : form ,
                    'title' : 'Student Registration'
                }
        return render(request, 'account/student_registration.html', context)



def RegistrationTeacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/home/')

    else:
        form = TeacherRegistrationForm
        context = {'form' : form,
                   'title' : 'Teacher Registration'
                   }
        return render(request, 'account/teacher_registration.html', context)