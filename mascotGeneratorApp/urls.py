from django.urls import path
from django.conf.urls import url, include


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about', views.about, name="about"),
    url(r'^generator', views.generator, name="generator"),
]