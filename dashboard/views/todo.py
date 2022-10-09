from django.shortcuts import render,redirect
from dashboard.models.todo import Todo
from dashboard.forms.todo import TodoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            todo = Todo(
                user =request.user,
                title = request.POST['title'],
                is_finished = finished
            )
            todo.save()
            messages.success(request,f"Todo Added from  {request.user.username}!!")
        return redirect('todo')    

    else:
        form = TodoForm()
    todos = Todo.objects.filter(user=request.user)
    if len(todos) ==0:
        todo_done = True
    else:
        todo_done = False
    context = {'form' : form ,'todos': todos,'todos_done': todo_done}

    return render ( request, 'dashboard/todo.html',context)

@login_required
def update_todo(request,pk=None):
    todo= Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')

@login_required
def delete_todo(request,pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('todo')

