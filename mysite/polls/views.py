#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404

from .models import Question

def index(request):
	#latest_question_list = Question.objects.order_by('-pub_date')[:2]
	#output = ', '.join([q.question_text for q in lasted_question_list])
	#return HttpResponse(output)
	#### 02
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	#context = {
	#	'latest_question_list': latest_question_list,
	#}
	#return HttpResponse(template.render(context, request))
	#### 03
	latest_question_list = Question.objects.order_by('-pub_date')[:2]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	#return HttpResponse("You're looking at question %s." % question_id)
	### 01
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist")
	#return render(request, 'polls/detail.html', {'question':question})
	### 02
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
	return HttpResponse("You're looking at the results of question %s" % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)


