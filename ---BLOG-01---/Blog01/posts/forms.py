from django import forms
from . import models

class PostForms(forms.ModelForm):
    class Meta: 
        model = models.Post
        fields = '__all__'

