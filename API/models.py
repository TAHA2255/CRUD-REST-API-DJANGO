from django.db import models
from django.urls import reverse

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    school = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    