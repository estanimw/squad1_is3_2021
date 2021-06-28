from django.urls import path
from .views import TaskView,TaskDetailView




urlpatterns = [
    path('tasks/', TaskView.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task')
]
