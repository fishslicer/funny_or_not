from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
#from .models import Question, Choice
from .models import Video, Comment

from .forms import VideoForm

#def index(request):
#    output = 'test format'
#    return HttpResponse(output)

class IndexView(generic.ListView):
    template_name = 'funny_or_not/index.html'
    context_object_name = 'latest_video_list'

    def get_queryset(self):
        return Video.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Video
    template_name = 'funny_or_not/detail.html'



def new_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = VideoForm()
    return render(request, '.html', {'form':form})

