from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import webbrowser


def index(request):
	template = loader.get_template('polls/index.html')
	# return render(request, 'polls/index.html')
	return HttpResponse(template.render(request))

def about(request):
	template = loader.get_template('polls/about.html')
	# return render(request, 'polls/index.html')
	return HttpResponse(template.render(request))

# def link(request):
# 	# template = loader.get_template('polls/about.html')
# 	# return render(request, 'polls/index.html')
# 	return HttpResponse(webbrowser.open('https://github.com/mishka28'))



# Create your views here.


