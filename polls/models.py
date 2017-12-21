from django.db import models

# Create your models here.
class Question(models.Model): # modles.Model: 継承元, OR マッパー？
    question_text = models.CharField(max_length=200) # 何でこいつだけ CamelCase?
    pub_date      = models.DateTimeField('date published') # オプションとして人間可読なフィールド名を指定

class Choice(models.Model):
    question    = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes       = models.IntegerField(default=0)
