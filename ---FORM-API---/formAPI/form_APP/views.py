from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    if (request.method == 'POST'):
        name= request.POST.get('username')
        email= request.POST.get('email')
        return render(request, 'form_APP/about.html', context={'name': name, 'email': email})
    else:
     return render(request, 'form_APP/about.html', context={'name': name, 'email': email})

def form(request):
    return render(request, 'form_APP/form.html')