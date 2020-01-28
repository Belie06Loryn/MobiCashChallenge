from django import forms
from django.contrib.auth.models import User
from .models import Add

class AddForm(forms.ModelForm):
    class Meta:
        model = Add
        exclude = ['user']
