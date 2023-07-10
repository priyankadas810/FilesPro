from django import forms
from .models import filecompare, wrd_to_pdf

class CompareForm(forms.ModelForm):
    class Meta:
        model = filecompare
        fields = ('Originalfile', 'Comparedfile')

class  WordForm(forms.ModelForm):
    class Meta:
        model = wrd_to_pdf
        fields = ('Wordfile',)