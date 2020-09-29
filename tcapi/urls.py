from django.contrib import admin
from django.urls import path
from tcapi import views

from .views import PageView

urlpatterns = [
    path('', PageView.as_view(template_name="index.html")),
    path('missing/', PageView.as_view(template_name="missing.html")),
    url(r'^api/tcapi$', views.user_list),
    url(r'^api/tcapi/(?P<pk>[0-9]+)$', views.user_detail),
    path('<str:template>', PageView.as_view()),
]

