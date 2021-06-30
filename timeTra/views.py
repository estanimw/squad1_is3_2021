from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views import View

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse

from .parser import *

from .models import Task
from . import models

def index(request):
    return HttpResponse("API de tareas de TimeTra APP.")

@api_view(['POST'])
def task_create(request):
    try:
        task = Task(**request.data)
        task.save()
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        if str(e) == "La tarea ya existe.":
            return Response(status = status.HTTP_409_CONFLICT)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def task_list(request):
    task_list = Task.getAllTasks()
    if len(task_list)>0:
        return Response(task_list, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT'])
def task(request,id):
    method = request.method
    if method == 'GET':
        return task_detail(request, id)
    elif method == 'PUT':
        return task_edit(request, id)




def task_detail(request,id):
    task = Task.getAllTasks().filter(id=id)
    if task:
        return Response(task, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



def task_edit(request,id):
    taskSet = Task.tasks.filter(id=id)
    task = taskSet.first()

    if task:
        try:
            (request.data).pop('id', None)
            task = task.modifyTask(**(request.data))
            task.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': str(e)},status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)