from .models import Subject, Topic, Subtopic, Video, Survey
from django.core import serializers
from django.core.handlers.base import logger
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib.auth import login, authenticate
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.db.models import Count, Q

from .forms import SignUpForm


# Create your views here.

@login_required
def homepage(request):
    return render(
        request,
        'home.html',
        context={'subject_list': Subject.objects.all()},
    )


def aboutpage(request):
    return render('about.html')


def contactpage(request):
    return render(request, 'contact.html')


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
            user_id = request.user.id
            user_answered_survey = Count('survey', filter=Q(survey__userId=user_id))
            # TODO get number of surveys from survey table and write to video table
            videos = Video.objects\
                .filter(subtopicid=request.GET['idsubtopic'])\
                .annotate(num_surveys=Count('survey')) \
                .annotate(user_answered_survey=user_answered_survey) \
                .values()

            data = json.dumps(list(videos), cls=DjangoJSONEncoder)
            response = HttpResponse()
            response['Content-Type'] = "text/javascript"
            response.write(data)
            return response
        except Exception as e:
            logger.exception("Failed to get videos" + str(e))
            return HttpResponse(status=500)
    else:
        return HttpResponse(status=400)


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

            survey, created = Survey.objects.get_or_create(video_id=video_id, userId=request.user.id)
            survey.mistakes = mistakes
            survey.presentation = presentation
            survey.informative = informative
            survey.quality = quality
            survey.relevant = '1'
            survey.level = 'Школьному'
            survey.save()

            video = Video.objects.filter(idvideo=video_id).first()
            video.available = '1'
            video.save()

            # Survey.create(mistakes=mistakes, presentation=presentation, informative=informative, quality=quality, videoid=video_id)
            return HttpResponse(status=200)
        except Exception as e:
            logger.exception("Failed to receive survey results", str(e))
            return HttpResponse(status=500)
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

            survey, created = Survey.objects.get_or_create(video_id=video_id, userId=request.user.id)
            survey.relevant = relevant
            survey.level = level
            survey.videoid = video_id
            survey.userId = request.user.id
            survey.save()

            video = Video.objects.filter(idvideo=video_id).first()
            video.available = '1'
            video.save()

            return HttpResponse(status=200)
        except Exception as e:
            logger.exception(str(e))
            return HttpResponse(status=500)
    else:
        return HttpResponse("Failed to receive results appropriate", status=400)


def set_video_not_available(request):
    if request.method == 'POST':
        try:
            args = {}
            args.update(csrf(request))
            video_id = request.POST['video_id']

            video = Video.objects.filter(idvideo=video_id).first()
            video.available = '0'
            video.save()

            return HttpResponse(status=200)
        except Exception as e:
            logger.exception(str(e))
            return HttpResponse(status=500)
    else:
        return HttpResponse("Failed to receive results video unavailable", status=400)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
