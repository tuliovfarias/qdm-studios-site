from django.http import Http404
from django.shortcuts import render
from .models import Post
from operator import itemgetter, attrgetter

# Create your views here.

def page_index(request):
    try:
        # post = Post.objects.get(id=1)
        posts = Post.objects.all()
        sorted_posts = sorted(posts, key=attrgetter('datetime'))
        latest_posts=sorted_posts[-6:]
    except:
        raise Http404()
    return render(request, "blog/index.html", {
        # 'title': post.title,
        # 'datetime': post.datetime,
        # 'text':post.text
        # 'titles': posts.title,
        # 'datetimes': posts.datetime,
        # 'texts': posts.text
        'posts': latest_posts
    })


def page_all_posts(request):
    pass


def page_selected_post(request):
    pass


def page_contato(request):
    pass


def page_sobre(request):
    pass
