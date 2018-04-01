# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Channel(models.Model):
    url = models.TextField(unique=True, primary_key=True)
    name = models.TextField()
    numberofsubscribers = models.IntegerField(db_column='numberOfSubscribers', blank=True, null=True)  # Field name made lowercase.
    averageviewsallvideos = models.IntegerField(db_column='averageViewsAllVideos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'channel'


class Subject(models.Model):
    idsubject = models.IntegerField(db_column='idSubject', primary_key=True)  # Field name made lowercase.
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'subject'


class Todayvideo(models.Model):
    idtodayvideo = models.IntegerField(db_column='idTodayVideo', primary_key=True)  # Field name made lowercase.
    name = models.TextField()
    url = models.TextField()
    channelurl = models.TextField(db_column='channelUrl', blank=True, null=True)  # Field name made lowercase.
    numberofviews = models.IntegerField(db_column='numberOfViews', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField()
    likes = models.IntegerField(blank=True, null=True)
    dislikes = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'todayVideo'


class Topic(models.Model):
    idtopic = models.IntegerField(db_column='idTopic', primary_key=True)  # Field name made lowercase.
    name = models.TextField()
    subjectid = models.IntegerField(db_column='subjectId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'topic'

    # has foreign key to subject - subjectId
class Subtopic(models.Model):
    idsubtopic = models.IntegerField(db_column='idSubTopic', primary_key=True)  # Field name made lowercase.
    name = models.TextField()
    topicid = models.IntegerField(db_column='topicId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subTopic'

    # has foreign key to topic - topicId,
class Video(models.Model):
    idvideo = models.IntegerField(db_column='idVideo', primary_key=True)  # Field name made lowercase.
    name = models.TextField()
    url = models.TextField()
    channelurl = models.TextField(db_column='channelUrl')  # Field name made lowercase.
    numberofviews = models.IntegerField(db_column='numberOfViews', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField()
    likes = models.IntegerField(blank=True, null=True)
    dislikes = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    subtopicid = models.IntegerField(db_column='subtopicId')
    available = models.IntegerField(db_column='available')

    # has foreign key to channel - channelUrl, on delete cascade
    class Meta:
        managed = False
        db_table = 'video'

class Survey(models.Model):
    idsurvey = models.IntegerField(db_column='idSurvey', primary_key=True)
    relevant = models.IntegerField(blank=True, null=True)
    level = models.TextField()
    mistakes = models.IntegerField(blank=True, null=True)
    presentation = models.IntegerField(blank=True, null=True)
    informative = models.IntegerField(blank=True, null=True)
    quality = models.IntegerField(blank=True, null=True)
    video = models.ForeignKey(Video, db_column='videoId', on_delete=models.CASCADE)
    userId = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey'

