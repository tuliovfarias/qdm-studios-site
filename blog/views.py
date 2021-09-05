#%%
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Slide
from operator import itemgetter, attrgetter

# Create your views here.

def page_index(request):
    try:
        # post = Post.objects.get(id=1)
        sledes = Slide.objects.all()
        latest_posts=get_latest_posts(6)
    except:
        raise Http404()
    return render(request, "blog/index.html", {
        'slides': sledes,
        'posts': latest_posts
    })

def get_latest_posts(number, exclude_slug=None):
        posts = Post.objects.exclude(slug=exclude_slug) #query all elements excluding that with the provided slug
        sorted_posts = sorted(posts, key=attrgetter('datetime'))
        print (sorted_posts)
        return(sorted_posts[-number:])

def page_all_posts(request):
    pass


def page_selected_post(request, post_slug):
    identified_post= Post.objects.get(slug=post_slug)
    other_posts= get_latest_posts(3,exclude_slug=post_slug)
    return render(request, "blog/post.html",{
        "post": identified_post,
        'other_posts': other_posts
    })

def page_contato(request):
    pass


def page_sobre(request):
    pass

# %%
