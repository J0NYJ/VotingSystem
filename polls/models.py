from django.db import models

# Create your models here.


# 问题
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")  # 双引号中定义的是在admin页面显示的verbose_name

    def __str__(self):
        return self.question_text


# 选择
class Choice(models.Model):
    question = models.ForeignKey("Question")
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
