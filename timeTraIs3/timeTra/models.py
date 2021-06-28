from django.db import models


# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    starting_date = models.IntegerField()
    estimated_time = models.IntegerField()
    time_spent = models.IntegerField(default=0)
    STATES = [
        ('Created','Created'),
        ('Paused','Paused'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    ]
    state = models.CharField(max_length=11, choices=STATES)
    tasks = models.Manager()

