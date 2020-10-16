from django.conf.urls import url
from tcapi import views

urlpatterns = [
    url(r'^api/tcapi/users', views.user_list),
    url(r'^api/tcapi/users/(?P<pk>[0-9]+)$', views.user_detail),
    url(r'^api/tcapi/posts', views.tweet_list),
]