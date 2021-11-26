from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Todo
from .forms import TodoForm


# Create your views here.
def delete(request, todo_id):
    task = Todo.objects.get(pk=todo_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    else:
        context = {'task': task}
        return render(request, 'delete.html', context)


def index(request):
    tasks = Todo.objects.all()
    form = TodoForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)


def addTodo(request):
    if request.method == 'POST':
        todo = request.POST['todo']
        Todo.objects.create(task_name=todo)
        return redirect('index')
    return render(request, 'index.html')


def update(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    form = TodoForm(request.POST or None, instance=todo)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'update.html', context)


def completed(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    form = TodoForm(instance=todo)
    form.completed = True
    return redirect('index')
