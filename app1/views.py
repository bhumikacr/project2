from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app1(request):
    return HttpResponse('This is frist of app1')
def app2(request):
    return HttpResponse('This is second of app1')
