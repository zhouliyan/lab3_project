"""lab3 URL Configuration

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
from django.contrib import admin
from django.contrib.auth.views import login, logout
import body.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'reg/$', body.views.register),
    url(r'profile/$', body.views.search),
    url(r'^search/$', body.views.search),
    url(r'^book_detail/(.*)/$', body.views.book_detail),
    url(r'^book_delete/(.*)/$', body.views.book_delete),
    url(r'^book_new/$', body.views.book_new),
    url(r'^book_renew/(.*)/$', body.views.book_renew),
    url(r'^author_add/$', body.views.author_add),   
]
