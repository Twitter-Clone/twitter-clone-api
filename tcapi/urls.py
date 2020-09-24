from django.contrib import admin
from django.urls import path

from .views import PageView

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', PageView.as_view(template_name="index.html")),
    path('missing/', PageView.as_view(template_name="missing.html")),
    path('<str:template>', PageView.as_view()),
    url(r'^api/tutorials$', views.tcapi),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tcapi),
    url(r'^api/tutorials/published$', views.tcapi)
]

