from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request,question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})
def result(request, question_id):
    response = 'patrzysz na wynik pytania nr %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('glosujesz na pytanie nr %s.' % question_id)
