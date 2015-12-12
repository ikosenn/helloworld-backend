from rest_framework import serializers

from helloworld.blog.models import (
    Category,
    BlogPost,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
