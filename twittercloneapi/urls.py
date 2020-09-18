from django.contrib import admin
from django.urls import path

from .views import PageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PageView.as_view()),
    path('<str:template>', PageView.as_view())
]

