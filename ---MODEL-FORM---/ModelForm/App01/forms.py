from django import forms
from . import models


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = models.Student
        fields = ("__all__")
        # labels = {
        #     'name': 'Student Name',
        #     'roll': 'Student Roll',
        #     'address': 'Student Address'
        # }
        # help_texts = {
        #     'name': 'Enter Your Full Name',
        #     'roll': 'What is your id?',
        #     'address': 'Your current home address'
        # }

        # widgets = {

        # }

        # error_messages={
        #     'name': {'required', 'Your name is required'}
        # }