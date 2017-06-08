from django import forms
from .models import Memo


class MemoModelForm(forms.ModelForm):
    
    class Meta:
        model = Memo
        fields = (
            'title',
            'description',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'cols': 40,
                                                 'rows': 10}),
        }


class MemoEditModelForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = (
            'title',
            'description',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'cols': 40,
                                                 'rows': 10}),
        }
