from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'site_name': 'blogs',
        'posts': posts
    }
    return render(request, 'index.html', context)

def aboutme(request):
    context = {
        'site_name': 'about'
    }
    return render(request, 'aboutme.html', context)
