
# Create your models here.
from django.db import models


class Vhigh(models.Model):
    question_text = models.CharField(max_length=200)
    sup = models.FloatField()
    
class High(models.Model):
    question_text = models.CharField(max_length=200)
    sup = models.FloatField()
    ids = models.AutoField(primary_key=True)
    def __High__(self):
        return self

    
class Med(models.Model):
    question_text = models.CharField(max_length=200)
    sup = models.FloatField()
    


#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)