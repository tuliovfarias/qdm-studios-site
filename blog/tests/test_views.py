from django.test import TestCase, Client
from blog.models import Post

from django.http import Http404
from django.shortcuts import render
from operator import itemgetter, attrgetter



class TestViews(TestCase):
    def test_page_selected_post(self):
        identified_post= Post.objects.get(slug='placas-acusticas-prontas')
        print(f'identified_post: {identified_post}')
        pass
        # other_posts= Post.objects.get(slug=post_slug)
        # return render(request, "blog/post.html",{
        #     "post": identified_post
        # })