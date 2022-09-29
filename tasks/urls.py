from venv import create
from django.urls import path
from .views import delete_task, list_tasks, create_task

urlpatterns = [
    path('', list_tasks),
    path('new_task/', create_task, name='create_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
]
