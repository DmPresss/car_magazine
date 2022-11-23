from django import forms
from django.forms import ValidationError
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 150:
            raise ValidationError('Length exceeds 150 characters')

        return title
