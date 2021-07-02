from django.db import models


# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=140)
    starting_date = models.BigIntegerField()
    estimated_time = models.IntegerField()
    STATES = [
        ('Created', 'Created'),
        ('Paused', 'Paused'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    state = models.CharField(max_length=11, default="Created", choices=STATES)
    tasks = models.Manager()


    def save(self, *arg, **args):
        if self.name == None or self.starting_date == None or self.name == '' or self.starting_date == '':
            print("HOLA")
            raise Exception("La tarea debe tener todos los campos requeridos.")
        elif len(self.description) > 140:
            raise Exception("La tarea debe tener una descripción de menos de 140 caracteres.")
        elif self in self.getAllTasks():
            raise Exception("La tarea ya existe.")
        else:
            super().save(*args, **args)


    @classmethod
    def getAllTasks(cls):
        return cls.tasks.values()


    @classmethod
    def delete(cls,id):
        task = cls.tasks.filter(id=id)
        if len(task) == 0:
            raise Exception("La tarea a eliminar no existe.")
        else:
            task.delete()


    def modifyTask(self, **argsToChange):
        keys = argsToChange.keys()
        for arg in keys:
            setattr(self, arg, argsToChange[arg])
        return self


    def __eq__(self, other):
        return isinstance(other, Task) and self.name == other.name and self.description == other.description and int(self.starting_date) == int(
            other.starting_date) and int(self.estimated_time) == int(other.estimated_time) and self.state == other.state

