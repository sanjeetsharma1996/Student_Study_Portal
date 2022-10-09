from django import forms

class ConversionForm(forms.Form):
    CHOICES = [('lenght','Lenght'),('mass','Mass')]
    measurement = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)

class ConversionLengthForm(forms.Form):
    CHOICES = [('yard','Yard'),('foot','Foot')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(attrs = {'type':'number','placeholder': 'Enter the Number'}))
    measure1 = forms.CharField(label='',widget=forms.Select(choices = CHOICES))
    measure2 = forms.CharField(label='',widget=forms.Select(choices = CHOICES))

class ConversionMassForm(forms.Form):
    CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(attrs = {'type':'number','placeholder': 'Enter the Number'}))
    measure1 = forms.CharField(label='',widget=forms.Select(choices = CHOICES))
    measure2 = forms.CharField(label='',widget=forms.Select(choices = CHOICES))

