from django.shortcuts import render,get_object_or_404
from . models import Post

# Create your views here.
posts = Post.objects.all()
context = {'posts': posts, }


def home(request):
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', )

