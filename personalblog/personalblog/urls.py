"""personalblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog import views

# We should switch these out with paths, figure out how to match the RegExp
# with whatever matching system path uses.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('blog/', views.index),
    path('resume/', views.resume),
    path('portfolio/', views.portfolio),
    url(
        r'^blog/view/(?P<slug>[^\.]+).html',
        views.view_post,
        name='view_blog_post'),
    url( # This is a RegExp that matches up a given slug with a template
        r'^blog/category/(?P<slug>[^\.]+).html',
        views.view_category,
        name='view_blog_category'),
]
