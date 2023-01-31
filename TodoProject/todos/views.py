from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse , HttpRequest
from .models import Todo

def list_todo_items(request):
    context={'todo_list':Todo.objects.all()}
    return render(request,'todos/todos_list.html',context)

def insert_todo_items(request:HttpRequest):
    todo=Todo(content=request.POST["content"])
    todo.save()
    return redirect('/todos/list/') 

def delete_todo_items(request,todo_id):
    todo_to_delete=Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/') 

    