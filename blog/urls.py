from .views import views, main, view_detail
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    # path('', views.base, name='base'),
    path('', main.main, name='main'),
    url(r'^img_uproad/$', view_detail.detail, name='detail'),
]
