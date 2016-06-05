"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings


app_patterns = [
    url(r'^blog/', include('helloworld.blog.urls', namespace='blog')),
    url(r'^users/',
        include('helloworld.user.urls', namespace='users')),
]

urlpatterns = [
    url(r'^api/', include(app_patterns, namespace="api")),
    url(r'^accounts/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^oauth2/', include(
        'oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]
