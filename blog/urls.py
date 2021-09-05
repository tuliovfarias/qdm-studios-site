from django.contrib import admin
from django.urls import path, include
from . import views
from blog.views import PostDetailView

urlpatterns = [
    path('', views.page_index, name='index'),
    path('posts', views.page_all_posts, name='all_posts'),
    path('post/<slug>', PostDetailView.as_view(), name='selected_post'),
    # path('post/<slug:post_slug>', views.page_selected_post, name='selected_post'),
    path('contato', views.page_contato, name='contato'),
    path('sobre', views.page_sobre, name='sobre'),
    # path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount'))  
]
