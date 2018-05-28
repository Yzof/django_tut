from django.contrib import admin
# You can access any .py file this way, atleast in django
from blog.models import Post, Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    # This will actually let posted be self-filled, excluding it from
    # user/admin control
    exclude = ['posted']
    # This prepopulated fields option will fill in the slug for us
    prepopulated_fields = { 'slug': {'title'}}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': {'title'}}
