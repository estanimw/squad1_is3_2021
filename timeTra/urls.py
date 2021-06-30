from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('task', views.task_create, name='task_create'),
    path('task/all', views.task_list, name='task_list'),
    path('task/<int:id>', views.task, name='task')
]
