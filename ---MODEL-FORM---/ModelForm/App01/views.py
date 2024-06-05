from django.shortcuts import render
from . import forms
# Create your views here.
def home(request):
    student = forms.StudentForm
    return render(request, 'home.html', {"student" : student})
