from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=1000)
    pubdate =models.DateTimeField("date published")
class choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
       
    
