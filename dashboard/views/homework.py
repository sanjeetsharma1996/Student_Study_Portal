from django.shortcuts import render,redirect
from dashboard.models.homework import Homework
from dashboard.forms.homework import HomeworkForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required


@login_required
def homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True 
                else:
                    finished = False
            except:
                finished = False
                
            Homeworks = Homework(
                user = request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished
            )
            Homeworks.save()
            messages.success(request,f"Notes Add from {request.user.username} successfully")
        return redirect('homework')

    else:
        form = HomeworkForm()
    homework = Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    context = {'homeworks': homework,
                'homeworks_done': homework_done,
                'form': form
                }

    return render ( request, 'dashboard/homework.html',context)

@login_required
def update_homework(request,pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True

    homework.save()
    return redirect('homework')


@login_required
def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')
