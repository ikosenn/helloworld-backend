from django.db import models


class Category(models.Model):
    """
    A model to store the category of the blog posts
    """

    name = models.CharField(max_length=50, default='')


class BlogPost(models.Model):
    """
    A model to store details pertaining to a blog post
    """

    tag = models.ManyToManyField(Category)
    user = models.ForeignKey(User)
    title = models.CharField(default='', max_length=255)
    slug = models.SlugField(default='', unique=True)
    views = models.IntegerField(default=0)
    content = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=0)
    image = models.ImageField(upload_to='blog')
    image_thumbnail = models.ImageField(upload_to='blog/thumbnail')
