# Create your views here.

from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views import View

from .models import Task


class TaskView(View):
    def get(self, request):
        task_list = list(Task.objects.all().values())
        return JsonResponse(task_list, safe=False)


class TaskDetailView(View):
    def get(self, request, pk):
        task = (Task.objects.get(pk=pk))
        return JsonResponse(model_to_dict(task), safe=False)
