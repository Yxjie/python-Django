from django.conf.urls import url
import booktest.views as views

urlpatterns = [
    url('^$', views.index),
    url('^index/$', views.load_html),
    url('^index/(\d+)/$', views.detail),
]
