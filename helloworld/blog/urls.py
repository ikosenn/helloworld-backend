from django.conf.urls import url

from helloworld.blog.views import (
    CategoryListView,
    CategoryDetailView,
    BlogPostListView,
    BlogPostDetailView,
)

urlpatterns = [
    url(r'^category/$', CategoryListView.as_view(), name='category'),
    url(r'^category/(?P<pk>[^/]+)/$',
        CategoryDetailView.as_view(), name='category_detail'),

    url(r'^post/$', BlogPostListView.as_view(), name='post'),
    url(r'^post/(?P<pk>[^/]+)/$',
        BlogPostDetailView.as_view(), name='post_detail'),
]
