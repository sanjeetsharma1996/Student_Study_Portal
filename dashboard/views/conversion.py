from django.shortcuts import render
from dashboard.forms.conversion import ConversionForm, ConversionLengthForm, ConversionMassForm


def conversion(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if request.POST['measurement'] == 'lenght':
            measuremet_form = ConversionLengthForm()
            context = {
                'form': form,
                'm_form': measuremet_form,
                'input': True
            }
            if 'input' in request.POST:
                first = request.POST.get('measure1')
                second = request.POST.get('measure2')
                input = request.POST['input']
                answer = ''
                if input and int(input) >= 0:
                    if first == 'yard' and second == 'foot':
                        answer = f"{input} yard = {int(input)*3} foot"
                    if first == 'foot' and second == 'yard':
                        answer = f"{input} foot = {int(input)/3} yard"
                context = {
                    'form': form,
                    'm_form': measuremet_form,
                    'input': True,
                    'answer': answer                  
                }

                
        if request.POST['measurement'] == 'mass':
            measuremet_form = ConversionMassForm()
            context = {
                    'form': form,
                    'm_form': measuremet_form,
                    'input': True
                }
            if 'input' in request.POST:
                first = request.POST.get('measure1')
                second = request.POST.get('measure2')
                input = request.POST['input']
                answer = ''
                if input and int(input) >= 0:
                    if first == 'pound' and second == 'kilogram':
                        answer = f"{input} pound = {int(input)*0.453592} kilogram"
                    if first == 'Kilogram' and second == 'pound':
                        answer = f"{input} Kilogram = {int(input)*2.20462} pound"
                context = {
                    'form': form,
                    'm_form': measuremet_form,
                    'input': True,
                    'answer': answer                  
                }
    else:
        form = ConversionForm()
        context ={
            'form':form, 
            'input': False
                }
    return render ( request, 'dashboard/conversion.html',context)
