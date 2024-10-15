# da

from django import forms
from .models import Task, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'descriptions', 'status', 'priority', 'due_date', 'assigned_to']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
