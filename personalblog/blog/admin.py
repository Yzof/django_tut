from django.contrib import admin
# You can access any .py file this way, atleast in django
from blog.models import Post, Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = { 'slug': {'title'}}
