from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todos
from .forms import TodoForm
# Create your views here.


def index(request):
    todos = Todos.objects.all()
    context = {
        'todos':todos
    }
    return render(request, "test.html", context)
    
def details(request, id):
    todo = Todos.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, "details.html", context)

def add(request):
    
    if(request.method == 'POST'):
        name = request.POST['name']
        Task = request.POST['Task']
        
        todo = Todos(name = name, Task = Task)

        todo.save()

        return redirect('/Todos')
    else:
        form = TodoForm()
        return render(request, "add.html", {'form': form})
