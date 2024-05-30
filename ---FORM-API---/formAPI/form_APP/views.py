from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return render(request, 'form_APP/about.html')