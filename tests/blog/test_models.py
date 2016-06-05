from django.utils import timezone
from rest_framework.test import APITestCase
from model_mommy import mommy
from helloworld.blog.models import (
    BlogPost,
    Comment,
    Category
)


class TestBlogPostModel(APITestCase):
    def test_str(self):
        blog_post = mommy.make(BlogPost, title="Panda")
        assert str(blog_post) == "Panda"

    def test_slug_field(self):
        title = 'some title'
        today = str(timezone.now().date())
        slug = 'some-title-' + today
        blog = mommy.make(BlogPost, title=title)
        assert blog.slug == slug


class TestCategoryModel(APITestCase):
    def test_str(self):
        category = mommy.make(Category, category="noma")
        assert str(category) == "noma"


class TestCommentModel(APITestCase):
    def test_str(self):
        comment = mommy.make(Comment, comment="wale_wabaya")
        assert str(comment) == "wale_wabaya"
