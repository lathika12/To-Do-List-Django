from django import forms
from . import models

class TodoListForm(forms.ModelForm):
    class Meta:
        model = models.TodoList
        fields = ('taskname','done')
