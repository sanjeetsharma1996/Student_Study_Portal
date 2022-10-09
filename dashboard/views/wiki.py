from django.shortcuts import render
from dashboard.forms.dashboardform import DashboardForm
import wikipedia


def wiki(request):
    if request.method == 'POST':
        text = request.POST['text']
        form = DashboardForm(request.POST)
        search = wikipedia.page(text)
        context = {
            'form': form,
            'title': search.title,
            'link':search.url,
            'details':search.summary
        }
        return render ( request, 'dashboard/wiki.html',context)
    else:
        form = DashboardForm()
        context = {'form': form}
    return render ( request, 'dashboard/wiki.html',context)