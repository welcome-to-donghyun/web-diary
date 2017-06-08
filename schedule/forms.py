import datetime
from django import forms
from .models import Memo, Diary


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


class DiaryModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DiaryModelForm, self).__init__(*args, **kwargs)
        self.fields['img'].required = False
        # self.fields['date'] = str(kwargs['data']['date'])


    class Meta:
        model = Diary
        fields = (
            'title',
            'description',
            'img',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'cols': 40,
                                                 'rows': 10}),
            'img': forms.FileInput(attrs={'clsas': 'btn btn-primary btn-block'}),

        }


class DiaryEditModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DiaryEditModelForm, self).__init__(*args, **kwargs)
        self.fields['img'].required = False


    class Meta:
        model = Diary
        fields = (
            'title',
            'description',
            'img',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'cols': 40,
                                                 'rows': 10}),
            'img': forms.FileInput(attrs={'clsas': 'btn btn-primary btn-block'}),
        }
