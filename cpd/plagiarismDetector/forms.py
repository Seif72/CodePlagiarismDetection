from django import forms
from .models import PythonFile

class PythonFileForm(forms.ModelForm):
    class Meta:
        model = PythonFile
        fields = ('file',)