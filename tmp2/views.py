from django.http import HttpResponse
from django.shortcuts import render
def ready(request):
    return HttpResponse("на старт")
# Create your views here.
def set1(request):
    return HttpResponse("Внимание")
def go(request):
    return HttpResponse("Марш")
from django.shortcuts import render

# Create your views here.
