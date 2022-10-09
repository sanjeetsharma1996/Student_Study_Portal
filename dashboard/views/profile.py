from django.shortcuts import render
from dashboard.models.homework import Homework
from dashboard.models.todo import Todo
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    homework = Homework.objects.filter(is_finished=False, user=request.user)
    todos = Todo.objects.filter(is_finished=False, user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False 

    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False 
    context = {
        'homework':homework,
        'todos': todos,
        'homework_done':homework_done,
        'todos_done':todos_done
    }
    return render(request,"dashboard/profile.html",context)
