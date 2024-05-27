from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def navigation(request):
    return render("Hello! This is --HOME-- Of the Navigation Directory")

def about(request):
    return render(request, "navigation/about.html")

def contact(request):
    return render(request, "navigation/contact.html")