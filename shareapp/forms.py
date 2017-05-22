from django import forms
from .models import bugshare

class mainform(forms.ModelForm):
    code =  forms.CharField( widget=forms.Textarea )
    bug =  forms.CharField( widget=forms.Textarea )
    comment =  forms.CharField( widget=forms.Textarea )
    class Meta:
        model = bugshare
        fields = ['name']
