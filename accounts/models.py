from django.db import models
from django.contrib.auth.models import User
from courses.models import *

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, default=None, on_delete = models.CASCADE)
    college = models.CharField(max_length=100, null=False, blank=False)
    contact = models.IntegerField(blank=False)
    profile_pic = models.ImageField(blank=True, null=True)
    fee_paid = models.BooleanField(null=False)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, default=None, on_delete = models.CASCADE)
    salary = models.IntegerField(null=False, blank=False)
    contact = models.IntegerField(blank=False)
    profile_pic = models.ImageField(blank=True, null=True)
    qualifications = models.TextField(blank=False)

    def __str__(self):
        return self.name