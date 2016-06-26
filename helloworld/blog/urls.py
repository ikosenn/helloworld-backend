from django.conf.urls import url
from rest_framework import routers

from helloworld.blog import views


router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'blog_posts', views.BlogPostViewSet)
router.register(r'comments', views.CommentViewSet)

ro_patterns = [
    url(r'^ro/categories/$',
        views.CategoryList.as_view(), name='categories_ro'),
    url(r'^ro/blog_posts/$',
        views.BlogPostList.as_view(), name='blog_posts_ro'),
    url(r'^ro/comments/$', views.CommentList.as_view(), name='comments_ro'),
]

urlpatterns = router.urls
urlpatterns += ro_patterns
