from django.conf.urls import url
from videoSiteApp import views

urlpatterns = [
    url(r'^$', views.homePage, name='home'),
    url('get_topic', views.get_topic, name='get_topic'),
    url('get_subtopic', views.get_subtopic, name='get_subtopic'),
    url('get_video_url', views.get_video_url, name='get_video_url'),
    url('set_video_survey_result', views.set_video_survey_result, name='set_video_survey_result'),
    url('set_video_not_available', views.set_video_not_available, name='set_video_not_available'),
    url('set_video_not_appropriate', views.set_video_not_appropriate, name='set_video_not_appropriate'),
    url('sign_up', views.sign_up, name='sign_up'),
]

