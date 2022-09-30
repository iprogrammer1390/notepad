from django import forms
from .models import Note

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'due_date', 'label']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'due_date':DatePickerInput(),
            'label':forms.Select(attrs={'class':'form-control'}),
        }
