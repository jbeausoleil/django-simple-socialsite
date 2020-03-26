from django.contrib import admin
from django.urls import path
from django.conf.urls import re_path, include

from . import views

urlpatterns = [
    re_path(r'^$', views.Homepage.as_view(), name='home'),
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('accounts.urls', namespace='accounts')),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^welcome/$', views.WelcomePage.as_view(), name='welcome'),
    re_path(r'^thanks/$', views.ThanksPage.as_view(), name='thanks'),
    re_path(r'^groups/', include('groups.urls', namespace='groups')),
    re_path(r'^posts/', include('posts.urls', namespace='posts')),
]
