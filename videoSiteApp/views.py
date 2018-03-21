from django.shortcuts import render
from .models import Subject, Topic, Subtopic
from django.core import serializers
from django.core.handlers.base import logger
from django.http import HttpResponse
# Create your views here.


def homePage(request):
    return render(
        request,
        'home.html',
        context={'subject_list': Subject.objects.all()},
    )

def aboutpage(request):
    return render('about.html')


def contactpage(request):
    return render('contact.html')


def get_topic(request):
    if request.method == 'GET':
        try:
            data = serializers.serialize('json', Topic.objects.filter(subjectid=request.GET['idsubject']))
            response = HttpResponse()
            response['Content-Type'] = "text/javascript"
            response.write(data)
            return response
        except Exception as e:
            logger.exception("Failed to get topics:" + str(e))
            return HttpResponse(status=500)
        else:
            return HttpResponse(status=404)

def get_subtopic(request):
    if request.method == 'GET':
        try:
            data = serializers.serialize('json', Subtopic.objects.filter(topicid=request.GET['idtopic']))
            response = HttpResponse()
            response['Content-Type'] = "text/javascript"
            response.write(data)
            return response
        except Exception as e:
            logger.exception("Failed to get subtopics:" + str(e))
            return HttpResponse(status=500)
        else:
            return HttpResponse(status=404)