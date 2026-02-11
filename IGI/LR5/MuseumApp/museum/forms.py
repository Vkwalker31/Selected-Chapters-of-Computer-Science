"""
Формы музея с валидацией на стороне сервера.
"""
from django import forms
from .models import Exhibit, Tour


class ExhibitForm(forms.ModelForm):
    class Meta:
        model = Exhibit
        fields = [
            'name', 'art_type', 'date_of_entry', 'hall', 'guardian',
            'description', 'image',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_of_entry': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
