import uuid

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    A model to store the category of the blog posts
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, default='')


class BlogPost(models.Model):
    """
    A model to store details pertaining to a blog post
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User)
    title = models.CharField(default='', max_length=255)
    slug = models.SlugField(default='', unique=True)
    views = models.IntegerField(default=0)
    content = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog')
    youtube_link = models.URLField(null=True)
