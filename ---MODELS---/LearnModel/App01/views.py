from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home(request):
    data = models.Students.objects.all()
    return render(request, 'home.html',{"data": data})


def delete_student(request, id):
    targeted_student = models.Students.objects.get(pk = id).delete()
    return redirect("homepage")