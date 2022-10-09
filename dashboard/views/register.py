from django.shortcuts import render,redirect
from dashboard.forms.user_register import UserregistrationForm
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = UserregistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username}")
            return redirect('login')
    else:
        form= UserregistrationForm()
    context = {
        'form': form
        }
    return render(request,'dashboard/register.html',context)