from django.shortcuts import render,redirect
from dashboard.models.notes import Notes
from dashboard.forms.notes import NotesForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required


@login_required
def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
            messages.success(request,f"Notes Add from {request.user.username} successfully")
        return redirect('note')

    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes, 'form':form }
    return render ( request, 'dashboard/notes.html',context)

@login_required
def delete_note(request,pk=None):
    note = Notes.objects.get(id=pk)
    note.delete()
    return redirect(notes)


class NotesDetailView(DetailView):
    model = Notes

# class NotesListView(ListView):
#     model = Notes