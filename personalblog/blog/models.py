from django.db import models

# Create your models here.
class Post(models.Model):
    # Defines the different characteristics of the elements
    # of the model
    title = models.CharField(max_length=100, unique=True)
    # A slug is the end bit of a url. ex: google.com/search,
    # search is the slug
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ("view_blog_post", None, { 'slug': self.slug })

class Category(models.Model)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ("view_blog_category", None, { 'slug': self.slug })