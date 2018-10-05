from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
    # url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
