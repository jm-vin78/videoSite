from django.conf.urls import url
from videoSiteApp import views

urlpatterns = [
    url(r'^$', views.homePage, name='home'),
    url('get_topic', views.get_topic, name='get_topic'),
    url('get_subtopic', views.get_subtopic, name='get_subtopic'),
]

