from django.shortcuts import render

# Create your views here.

def page_index(request):
    return render(request, "blog/index.html")

def page_all_posts(request):
    pass

def page_selected_post(request):
    pass

def page_contato(request):
    pass

def page_sobre(request):
    pass