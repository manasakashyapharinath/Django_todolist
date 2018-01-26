from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todos
from .forms import TodoForm
from django.views.decorators.http import require_POST
#from .forms import TodoForm



def index(request):
 todo_list = todos.objects.order_by('id')
 form = TodoForm()
 context = {'todo_list' : todo_list, 'form' : form}
 return render(request, 'todos/index.html', context)

@require_POST
def addTodo(request):
 form = TodoForm(request.POST)
 if form.is_valid():
  new_todo = todos(text=request.POST['text'])
  new_todo.save()
  return redirect('index')


'''def completeTodo(request, todo_id):
 todo = todos.objects.get(pk=todo_id)
 todo.complete = True
 todo.save()
 return redirect('index')'''

@require_POST
def completeTodo(request):
 form = request.POST.getlist('check[]')
 print(form)
 
 for i in range(len(form)):
  todo = todos.objects.get(pk=int(form[i]))
  if 'delete' in request.POST:
   print ('delete')
   todo.delete()
  elif 'complete' in request.POST:
   todo.complete = True
   todo.save()	
 return redirect('index')
