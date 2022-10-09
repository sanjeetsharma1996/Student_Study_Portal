from dashboard.models.notes import Notes
from django import forms


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']
        
class DateInput(forms.DateInput):
    input_type = 'date'
