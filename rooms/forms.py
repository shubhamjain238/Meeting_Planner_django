from django import forms
from .models import Room

class New_Room(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'