from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_minio import settings


urlpatterns = [
    # path('',include('apps.urls')),
    path('admin/', admin.site.urls),
]
