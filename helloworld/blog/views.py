from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from helloworld.blog.models import (
    Category,
    Comment,
    BlogPost
)

from helloworld.blog.serializers import (
    CategorySerializer,
    BlogPostSerializer,
    CommentSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)


class BlogPostList(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (AllowAny,)
