from django.conf.urls import url
from videoSiteApp import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url('get_topic', views.get_topic, name='get_topic'),
    url('get_subtopic', views.get_subtopic, name='get_subtopic'),
    url('get_video_url', views.get_video_url, name='get_video_url'),
    url('set_video_survey_result', views.set_video_survey_result, name='set_video_survey_result'),
    url('set_video_not_available', views.set_video_not_available, name='set_video_not_available'),
    url('set_video_not_appropriate', views.set_video_not_appropriate, name='set_video_not_appropriate'),
    url('signup', views.signup, name='signup'),
    url('login', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url('logout', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url('contact', views.contactpage, name='contact')
]

