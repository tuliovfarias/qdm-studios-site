from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.page_index, name='index'),
    path('posts', views.page_all_posts, name='all_posts'),
    path('post/<slug:post_slug>', views.page_selected_post, name='selected_post'),
    path('contato', views.page_contato, name='contato'),
    path('sobre', views.page_sobre, name='sobre')    
]
