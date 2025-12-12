from django import forms 
from mainapp.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields= ["task",'is_completed']