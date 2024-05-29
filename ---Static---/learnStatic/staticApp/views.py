from django.shortcuts import render

# Create your views here.
def github(request):
    return render(request, 'staticApp/github.html')
