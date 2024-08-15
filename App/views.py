from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import get_object_or_404

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)

    return render(request, 'index.html', {'tasks': tasks})

def mark_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
