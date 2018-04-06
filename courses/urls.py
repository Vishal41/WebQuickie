from django.conf.urls import url
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^list/$', views.CourseListView.as_view(), name='list'),
    url(r'^list/(?P<pk>\d+)$', views.CourseDetailView.as_view(), name='detail'),
    url(r'^create/$', views.CourseCreateView.as_view(), name='create'),
]
