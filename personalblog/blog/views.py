from django.shortcuts import render, render_to_response, get_object_or_404
from personalblog.blog.models import Post, Category
# Create your views here.

def index(request):
    # This index request only loads in 5 at a time
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })

def view_post(request, slug):
    # render_to_response takes in a Template name, and a json request
    # package
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        posts: Post.objects.filter(category=category)[:5]
    })
