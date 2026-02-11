"""
Формы страниц с серверной валидацией.
"""
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Форма отзыва: текст, оценка. Имя подставится из user."""
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Текст отзыва'}),
        }
