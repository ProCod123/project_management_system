from django import forms
from .models import TaskDocuments

class TaskDocumentForm(forms.ModelForm):
    class Meta:
        model = TaskDocuments
        fields = ['file', 'description'] 