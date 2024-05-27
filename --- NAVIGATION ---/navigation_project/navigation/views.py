from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def navigation(request):
    return render("Hello! This is --HOME-- Of the Navigation Directory")

def about(request):
    my_about = {
        'Name': 'JY-97',
        'Age': '24',
        'Phone': '01754623158'
    }
    return render(request, "navigation/about.html", context=my_about)

def contact(request):
    return render(request, "navigation/contact.html")