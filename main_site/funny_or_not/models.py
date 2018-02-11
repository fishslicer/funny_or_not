from django.db import models

#video posted on site
class Video(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    link = models.CharField(max_length=2000)
    funny = models.IntegerField(default=0)
    not_funny = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date posted')

#comment to specific video
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    funny = models.BooleanField(default=FALSE)

    
