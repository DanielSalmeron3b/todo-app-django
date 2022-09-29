from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'list_tasks.html', {'tasks': tasks})

def create_task(request):
    task = Task(
        title=request.POST['title'],
        description=request.POST['description'],
        )
    task.save()
    return redirect('/tasks/')

def delete_task(request, id):
    deleted_task = Task.objects.get(id=id)
    deleted_task.delete()
    return redirect('/tasks/')