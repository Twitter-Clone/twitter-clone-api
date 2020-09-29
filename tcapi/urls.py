from django.conf.urls import url
from tcapi import views

urlpatterns = [
    url(r'^api/tcapi$', views.user_list),
    url(r'^api/tcapi/(?P<pk>[0-9]+)$', views.user_detail),
    
]

