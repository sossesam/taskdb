
from django import forms
from .models import taskD

class TaskForm(forms.ModelForm):
    class Meta:
        model = taskD
        fields = ['task','desription']
    
