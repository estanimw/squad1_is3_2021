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

    # data = request.data
    # task = Task.objects.create(**data)
    # return Response(task)

    try: name = request.data['name']
    except: name = None

    try: description = request.data['description']
    except: description = None

    try: starting_date = request.data['starting_date']
    except: starting_date = None

    try: estimated_time = request['estimated_time']
    except: estimated_time = None

    try: time_spent = request.data['time_spent']
    except: time_spent = None

    try: state = request.data['state']
    except: state = None
    #return Response(**(request.data))
    try:
        task = Task(
            name=name,
            description=description,
            starting_date=starting_date,
            estimated_time=estimated_time,
            time_spent=time_spent,
            )
        data = request.data
        #return Response(request.data)
        task = Task.objects.create(**(request.data))
        return Response(request.data)
        task.save()
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def task_list(request):
    try:
        task_list = list(Task.getAllTasks().values())
        if len(task_list)>0:
            return Response(task_list, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class TaskDetailView(View):
    def get(self, request, pk):
        task = (Task.objects.get(id=pk))
        return JsonResponse(model_to_dict(task), safe=False)
