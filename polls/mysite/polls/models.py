from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
    question_text= models.CharField(max_length=1000)
    pubdate =models.DateTimeField("date published")
    def was_published_recently(self):
        return self.pubdate >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text
class choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
    def __str__(self) :
        return self.choice
    
       
    
