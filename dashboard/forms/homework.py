from dashboard.models.homework import Homework
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due': DateInput}
        fields = ['subject','title','description','due','is_finished']