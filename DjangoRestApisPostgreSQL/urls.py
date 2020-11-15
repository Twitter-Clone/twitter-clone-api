from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^', include('tcapi.urls')),
    path('tcapi/', include('tcapi.urls')),
    path('token-auth/', obtain_jwt_token)
]
