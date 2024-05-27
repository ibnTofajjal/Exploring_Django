from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def navigation(request):
    return render("Hello! This is --HOME-- Of the Navigation Directory")

def about(request):
    my_about = {'author' : 'Rahim', 'age' : 5, 'lst' : ['python','is','best'], 'birthday' : datetime.datetime.now(), 'val' : '' ,'courses' : [
        
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 10000 
        },
        {
            'id' : 3,
            'name' : 'C',
            'fee' : 1000 
        },
    ]}
    return render(request, "navigation/about.html", context=my_about)

def contact(request):
    return render(request, "navigation/contact.html")