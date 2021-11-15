from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Todo


# Create your views here.
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


def delete(request):
    render("Delete")


def update(request):
    render("Update")
