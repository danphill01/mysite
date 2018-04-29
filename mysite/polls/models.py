import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
# we could also default to now() for your time zone
#   pub_date = models.DateTimeField('date published', auto_now_add=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now() 
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #give the function some attributes to make it display better in admin page
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    content = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['-votes',]
    
    def __str__(self):
        return self.choice_text

    
