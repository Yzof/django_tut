from django.shortcuts import render, render_to_response, get_object_or_404
from personalblog.blog.models import Post, Category
# Create your views here.

def index(request):
    # This index request only loads in 5 at a time
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })

def view_post(request):
    return render_to_response('view_post.html', {
    
    })
