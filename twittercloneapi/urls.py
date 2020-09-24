from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url


urlpatterns = [
    path('polls/', include('tcapi.urls')),
    path('admin/', admin.site.urls),
]
