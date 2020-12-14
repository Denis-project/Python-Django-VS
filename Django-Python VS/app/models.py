"""
Definition of models.
"""

from django.db import models

# Create your models here.



class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    def __str__(self):
        return '{}'.format(self.name, surname)






