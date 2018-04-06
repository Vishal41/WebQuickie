from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    url(r'^registration/student$', views.RegistrationStudent, name = 'registration_student'),
    url(r'^registration/student$', views.RegistrationTeacher, name = 'registration_teacher')
]