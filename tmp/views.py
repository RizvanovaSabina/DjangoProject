from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Всем привет!")
# Create your views here.
def kd(request):
    return HttpResponse("Как делишки?")
def chd(request):
    return HttpResponse("Что делаешь??")