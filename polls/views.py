from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from .models import *


# 首页，展示所有问题
def index(req):
    lastest_question_list = Question.objects.all()
    return render(req, "polls/index.html", locals())


# 展示单个问题的所有选项
def detail(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/detail.html", locals())


# 查看投票结果
def results(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/results.html", locals())


# 选择投票
def vote(req, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, "polls/detail.html", {"question": p, "error_message": "You did't select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse("polls:results", args=(p.id,)))
