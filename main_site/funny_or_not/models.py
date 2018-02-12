from django.db import models
from django.forms import ModelForm

#video posted on site
class Video(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    link = models.CharField(max_length=2000)
    funny = models.IntegerField(default=0)
    not_funny = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date posted')

    #def get_comment_count(self):
    #    return Video.comment

    def get_funny_percent(self):
        if(self.funny == 0 and self.not_funny == 0):
            return 50
        else:
            return round((self.funny) * 100 / (self.funny + self.not_funny),1)

    def increment_funny(self):
        print("funny")
        self.funny+=1

    def increment_not_funny(self):
        print("not funny")
        self.not_funny+=1

    def get_funny(self):
        if(self.funny < 1000):
            return self.funny;
        elif(self.funny < 1000000):
            return str(int(self.funny/1000)) + "K"
        else:
            return str(int(self.funny/1000/1000)) + "M"

    def get_not_funny(self):
        if(self.not_funny < 1000):
            return self.not_funny;
        elif(self.not_funny < 1000000):
            return str(int(self.not_funny/1000)) + "K"
        else:
            return str(int(self.not_funny/1000/1000)) + "M"





#comment to specific video
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    funny = models.BooleanField(default=False)



    
