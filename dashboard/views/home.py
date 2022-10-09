from django.shortcuts import render,redirect

def home(request):
    return render ( request, 'dashboard/home.html') 