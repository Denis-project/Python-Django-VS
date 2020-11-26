"""
Definition of models.
"""

from django.db import models

# Create your models here.

# БД

class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    def __str__(self):
         return self.name


