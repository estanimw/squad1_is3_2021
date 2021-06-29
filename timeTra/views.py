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
        return Response(status = status.HTTP_400_BAD_REQUEST)


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
