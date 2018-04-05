from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
#    return HttpResponse(output)
    return HttpResponse(template.render(context, request))

#Here's the final short (magic) version that doesn't require HttpResponse and loader imports 
# from django.shortcuts import render
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

    
def detail(request, question_id):
    return HttpResponse("You're looking at question {}".format(question_id))


def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question {}.".format(question_id))
