from django.http import HttpResponse
from django.shortcuts import render
def facts(request):
    return HttpResponse("2 забавных факта о дельфинах")
# Create your views here.
def fact1(request):
    return HttpResponse("Рождение дельфина начинается с хвоста, а не с головы")
def fact2(request):
    return HttpResponse("Молодые дельфины остаются с матерью в течение 2-3 лет")
