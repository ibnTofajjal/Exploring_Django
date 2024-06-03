from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    data = models.Students.objects.all()
    return render(request, 'home.html',{"data": data})