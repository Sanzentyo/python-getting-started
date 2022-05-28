from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting
import os

def index(request):
    times = int(os.environ.get('TIMES', 3))
    return HttpResponse('Hello! ' * times + "/nas the nights reincarnation")
"""
def index(request):
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
"""


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
