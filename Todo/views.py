from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Todo


# Create your views here.
def delete(request, todo_id):
    tasks = Todo.objects.get(pk=todo_id)
    context = {'tasks': tasks}
    return render(request, 'delete.html', context)


def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def addTodo(request):
    if request.method == 'POST':
        todo = request.POST['todo']
        Todo.objects.create(task_name=todo)
        return redirect('index')
    return render(request, 'index.html')

def update(request):
    render("Update")
