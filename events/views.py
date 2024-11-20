from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render



def index(request):

    return render(request, "events/index.html", )

def detail(request, question_id):

    return render(request, "events/detail.html", )

