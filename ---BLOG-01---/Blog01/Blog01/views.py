from django.http import HttpResponse
from django.shortcuts import render, redirect
from posts.models import Post

def home(requset):
    data = Post.objects.all()
    return render(requset, 'home.html', {"posts": data}) 