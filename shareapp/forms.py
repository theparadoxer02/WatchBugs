from django import forms
from .models import bugshare

class mainform(forms.ModelForm):
    class Meta:
        model = bugshare
        fields = ['name','url','code','bug','comment']
