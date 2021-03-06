from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Post, Category
# Create your views here.

def home(request):
    return render_to_response('home.html')

def resume(request):
    return render_to_response('resume.html')

def portfolio(request):
    return render_to_response('portfolio.html')

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
    # the posts
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })
