from django.http import HttpResponse

from .models import Question


def root_index(request):
    return HttpResponse("this is root index page")
    
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("you rae looking at quesition %s." % question_id)

def results(request, question_id):
    response = "your are looking at the results of quesition %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you are voting on quesition %s." % question_id)