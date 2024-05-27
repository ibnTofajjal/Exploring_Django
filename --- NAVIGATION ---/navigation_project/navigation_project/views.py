from django.shortcuts import render

# Home Route
def home(request):
    return render(request, 'index.html')