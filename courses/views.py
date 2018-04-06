from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Course

# Create your views here.

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/course_create.html'
