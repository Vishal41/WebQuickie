from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    #url(r'^$', views.home, name= 'home'),
    url(r'^registration/student$', views.RegistrationStudent, name = 'registration_student'),
    url(r'^registration/teacher$', views.RegistrationTeacher, name = 'registration_teacher'),
    url(r'^login/', login, {'template_name':'account/login.html'}),
    url(r'^logout/', logout, {'account/logout.html'})
]