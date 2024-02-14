from django.db import models
from django.utils import timezone
import datetime

##copied from Creating models djandoproject documentation 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
from django.db import models

class Artist(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Album(models.Model):
  title = models.CharField(max_length=100)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

class Song(models.Model):
  title = models.CharField(max_length=100)
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

