from helloworld.common.serializers import AuditFieldsMixin
from helloworld.blog.models import (
    Category,
    BlogPost,
    Comment,
)


class CategorySerializer(AuditFieldsMixin):
    class Meta:
        model = Category


class BlogPostSerializer(AuditFieldsMixin):
    class Meta:
        model = BlogPost
        read_only_fields = ('comments',)


class CommentSerializer(AuditFieldsMixin):
    class Meta:
        model = Comment
