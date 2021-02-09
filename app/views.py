from django.shortcuts import render 
from django.http import HttpResponse


# HttResponse Handle's responses and requests
# Render returns a rendered template takes the first argument as a request. By default it searches the templates folder.


# Create your views here as functions.

# These functions handle traffic directed towards them

posts = [
    {
        'author': 'first',
        'title': 'post',
        'content': 'first post',
        'date': 'some date',
    },
    {
        'author': '2nd',
        'title': 'post',
        'content': 'second post',
        'date': 'another date',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)   # context is an argument that passes data in context dict into page

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})

def search(request):
    return render(request, 'blog/search.html', {'title': 'find your room'})