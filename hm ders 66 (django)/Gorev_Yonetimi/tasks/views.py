from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def task_list(request):
    tasks  = Task.objects.all()
    return render(request, "task_list.html", {"tasks": tasks})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "create_task.html", {"form": form})