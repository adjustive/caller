from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django import forms
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render_to_response('master.html', { 'title' : 'Model Run'} , context_instance=RequestContext(request))
