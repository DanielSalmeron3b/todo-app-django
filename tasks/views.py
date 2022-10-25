from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

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

def edit_task(request, id):
    task = Task.objects.get(id=id)
    forms = TaskForm(request.POST or None, instance=task)
    if forms.is_valid() and request.POST:
        forms.save()
        return  redirect('/tasks/')
    return render(request, 'edit_task.html', {'forms': forms})