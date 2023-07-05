from django.shortcuts import render,loader,get_object_or_404
from .models import Question,choice
from django.urls import reverse
from django.http import HttpResponse,Http404,HttpResponseRedirect
def index(request):
    latest_question_list = Question.objects.order_by("-pubdate")[:5]
    template=loader.get_template("polls/index.html")
    content={
        "latest_question_list":latest_question_list
    }
    return HttpResponse(template.render(content,request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {"question": question})
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, choice.DoesNotExist):
        
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))
