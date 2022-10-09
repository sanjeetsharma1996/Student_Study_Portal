
from django.shortcuts import render
from dashboard.forms.dashboardform import DashboardForm
from django.contrib import messages
from youtubesearchpython import VideosSearch
import requests


def youtube(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text,limit=10)
        result_list = []
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'duration':i['title'],
                'title':i['duration'],
                'thumbnails':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'viewcount':i['viewCount']['short'],
                'publishedTime':i['publishedTime'],
            }
            desc =''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] =desc
            result_list.append(result_dict)
            context = {'form': form, 'results':result_list}

        return render(request,'dashboard/youtube.html',context)
    else:
        form = DashboardForm()
    context = {'form' : form }
    return render ( request, 'dashboard/youtube.html',context)