from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
def clk(request):
    return render_to_response('clk.html',locals())
def test(request):
    return render_to_response('test.html',locals())
