from django.db import models

# Create your models here.
class Post(models.Model):
    # The following lines of code define the different characteristics
    # for the elements of the model
    title = models.CharField(max_length=100, unique=True)
    # A slug is the end bit of a url. ex: google.com/search,
    # search is the slug
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)

    # This deviates from the standard tutorial. Notes above about what
    # the ManyToManyField is in the README
    category = models.ManyToManyField('blog.Category')

    # This will order the posts by ascending order. add a - to order desc
    # check README for notes
    ordering = ['posted']

    # The following function  sets the text reference for each record.
    # This is used mainly in the automated django admin, but this is
    # still available to use on your own site.
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
