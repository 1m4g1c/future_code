from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
# Create your views here.
def home(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'site_name': 'blogs',
        'posts': posts,
        'comments': comments,
    }
    return render(request, 'index.html', context)

def aboutme(request):
    context = {
        'site_name': 'about'
    }
    return render(request, 'aboutme.html', context)

def new_comment(request):
    text = request.GET['text']
    post_id = request.GET['post_id']
    comment = Comment(post_id=post_id, text=text)
    comment.save()
    return redirect('/')
