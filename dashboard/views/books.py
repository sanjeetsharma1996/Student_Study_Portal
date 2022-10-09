from django.shortcuts import render
from dashboard.forms.dashboardform import DashboardForm
import requests

def books(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url = 'https://www.googleapis.com/books/v1/volumes?q='+text
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][0]['volumeInfo']['imageLinks'].get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink')

            }
            result_list.append(result_dict)
            context ={
                'form':form,
                'results': result_list
            }
        return render ( request, 'dashboard/books.html',context)
    else:
        form = DashboardForm()
    context = {'form': form}
    return render ( request, 'dashboard/books.html',context)
