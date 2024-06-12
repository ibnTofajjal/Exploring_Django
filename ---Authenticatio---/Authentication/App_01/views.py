from django.shortcuts import render
from django.http import HttpResponse
from App_01 import forms

# Create your views here.
def home(request):
   if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
   else:
      form = forms.RegisterForm()
   return render(request, "home.html", {'forms': form})