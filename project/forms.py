from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
class RegForm(ModelForm):
    class Meta:
        model = User 
        fields = ['username','email','password','first_name', 'last_name']
