from django.shortcuts import render
from .models import Subject, Topic, Subtopic, Video
from django.core import serializers
from django.core.handlers.base import logger
from django.http import HttpResponse
from django.template.context_processors import csrf


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


def get_video_url(request):
    if request.method == 'GET':
        try:
            data = serializers.serialize('json', Video.objects.filter(subtopicid=request.GET['idsubtopic']))
            response = HttpResponse()
            response['Content-Type'] = "text/javascript"
            response.write(data)
            return response
        except Exception as e:
            logger.exception("Failed to get videos" + str(e))
            return HttpResponse(status=500)
        else:
            return HttpResonse(status=400)


def set_video_survey_result(request):
    if request.method == 'POST':
        try:
            args = {}
            args.update(csrf(request))
            mistakes = request.POST['mistakes']
            presentation = request.POST['presentation']
            informative = request.POST['informative']
            quality = request.POST['quality']
            video_id = request.POST['video_id']

            video = Video.objects.filter(idvideo=video_id).first()
            #TODO write to DB
            return HttpResponse(status=200)
        except Exception as e:
            logger.exception(str(e))
        else:
            return HttpResponse(status=400)


def set_video_not_appropriate(request):
    if request.method == 'POST':
        try:
            args = {}
            args.update(csrf(request))
            relevant = request.POST['relevant']
            level = request.POST['level']
            video_id = request.POST['video_id']

            video = Video.objects.filter(idvideo=video_id).first()
            #TODO write to DB
            return HttpResponse(status=200)
        except Exception as e:
            logger.exception(str(e))
        else:
            return HttpResponse(status=400)


def set_video_not_available(request):
    if request.method == 'POST':
        try:
            args = {}
            args.update(csrf(request))
            video_id = request.POST['video_id']

            video = Video.objects.filter(idvideo=video_id).first()
            #TODO write to DB
            return HttpResponse(status=200)
        except Exception as e:
            logger.exception(str(e))
        else:
            return HttpResponse(status=400)