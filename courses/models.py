from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    starting_on = models.DateField()

    def __str__(self):
        return self.name
