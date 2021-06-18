from django.db import models


# Create your models here.

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    starting_date = models.DateField()
    estimated_time = models.IntegerField()
