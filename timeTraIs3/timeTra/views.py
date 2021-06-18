from django.shortcuts import render

# Create your views here.

from django.views import View
from .models import Task
from django.http import JsonResponse
from django.forms.models import model_to_dict


class TaskView(View):
    def get(self, request):
        task_list = list(Task.objects.all().values())
        return JsonResponse(task_list, safe=False)


class TaskDetailView(View):
    def get(self, request, pk):
        task = (Task.objects.get(pk=pk))
        return JsonResponse(model_to_dict(task), safe=False)
