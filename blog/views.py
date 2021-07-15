from django.http import Http404
from django.shortcuts import render
from .models import Post

# Create your views here.

def page_index(request):
    try:
        post = Post.objects.get(id=1)
    except:
        raise Http404()
    return render(request, "blog/index.html",{
        'title': post.title,
        'datetime': post.datetime,
        'text':post.text
    })

def page_all_posts(request):
    pass

def page_selected_post(request):
    pass

def page_contato(request):
    pass

def page_sobre(request):
    pass