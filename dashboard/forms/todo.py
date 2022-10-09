from dashboard.models.todo import Todo
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model =Todo
        fields = ['title']