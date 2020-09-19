from django.contrib import admin
from django.urls import path

from .views import PageView

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', PageView.as_view(template_name="index.html")),
    path('missing/', PageView.as_view(template_name="missing.html"))
    path('<str:template>', PageView.as_view()),
]

