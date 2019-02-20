from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.
def todoView(request):
    all_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_items})

def addTodo(request):
    new_item = TodoItem(title=request.POST['title'], content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    to_be_removed = TodoItem.objects.get(id=todo_id)
    to_be_removed.delete()
    return HttpResponseRedirect('/todo/')