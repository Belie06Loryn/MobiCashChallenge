from django import forms
from django.contrib.auth.models import User
from .models import Add

class AddForm(forms.ModelForm):
    class Meta:
        model = Add
        name = forms.CharField(widget=forms.TextInput(attrs={'id': 'name'}))
        nid = forms.CharField(widget=forms.TextInput(attrs={'id': 'nid'}))
        fone = forms.CharField(widget=forms.TextInput(attrs={'id': 'fone '}))
        exclude = ['user']
