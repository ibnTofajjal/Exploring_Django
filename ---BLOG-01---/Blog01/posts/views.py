from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from posts.models import Post

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForms(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect("add_post")
    else:
        post_form = forms.PostForms()
    return render(request, "add_post.html", {"forms": post_form}) 


def edit_post(request, id):
    post = Post.objects.get(pk=id) # Get the post object through specific id.
    post_form = forms.PostForms(instance=post)

    if request.method == 'POST':
        post_form = forms.PostForms(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect("homepage")
    return render(request, "add_post.html", {"forms": post_form}) 


def delete_post(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("homepage")