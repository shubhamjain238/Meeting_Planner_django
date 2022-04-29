from django import forms
from .models import Meeting
from django.forms import DateInput, TimeInput, TextInput
from datetime import date
from django.core.exceptions import ValidationError

class New_meeting(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'type': ''}),
            'date' : DateInput(attrs={'type': 'date'}),
            'time': TimeInput(attrs={'type': 'time'}),
            'duration' : TextInput(attrs={'type': 'number', 'min': 1, 'max': 4})
        }

    def clean_date(self):
        if self.cleaned_data.get('date') < date.today():
            raise ValidationError('Meeting cannot occur in past date')
        return self.cleaned_data.get('date')
