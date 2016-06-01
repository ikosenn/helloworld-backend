from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from helloworld.common.models import AbstractBase


class Category(AbstractBase):
    """
    A model to store the category of the blog posts
    """

    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Comment(AbstractBase):
    """
    A BlogPost can have one or more comments
    """
    comment = models.TextField()

    def __str__(self):
        return self.comment


class BlogPost(AbstractBase):
    """
    A model to store details pertaining to a blog post
    """

    categories = models.ManyToManyField(Category)
    comments = models.ManyToManyField(Comment)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    views = models.IntegerField(default=0)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug_field = self.title + '-' + str(timezone.now().date())
        self.slug = slugify(slug_field)
        super().save(*args, **kwargs)
