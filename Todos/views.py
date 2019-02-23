from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos
from .forms import TodoForm
# Create your views here.


def index(request):
    todos = Todos.objects.all()
    context = {
        'todos':todos
    }
    return render(request, "index.html", context)
    
def details(request, id):
    todo = Todos.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, "details.html", context)

def add(request):
    
    if(request.method == 'POST'):
        return
    else:
        form = TodoForm()
        return render(request, "add.html", {'form': form})
