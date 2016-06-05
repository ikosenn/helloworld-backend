from rest_framework import routers

from helloworld.blog import views


router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'blog_posts', views.BlogPostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = router.urls
