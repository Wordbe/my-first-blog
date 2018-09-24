from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    path('', views.base, name='base'),
]