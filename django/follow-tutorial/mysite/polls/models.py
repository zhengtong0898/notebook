import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        # problem
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        #
        # fix:
        now = timezone.now()
        # now - datetime.datetime(days=1) == 昨天
        # 昨天 <= self.pub_date           == 一天内发布的
        # self.pub_date <=               == 不能是未来的时间
        return now - datetime.datetime(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)