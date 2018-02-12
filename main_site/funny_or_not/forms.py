from django import forms
from django.forms import ModelForm
from .models import Video, Comment


class VideoForm(ModelForm):
    """
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    link = models.CharField(max_length=2000)
    funny = models.IntegerField(default=0)
    not_funny = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date posted')
    """
    class Meta:
        model = Video
        fields = ['title', 'desc', 'link']


