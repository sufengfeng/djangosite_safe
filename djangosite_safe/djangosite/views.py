import json
import datetime
import json
import time
from random import random
from re import search

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse


# Create your views here.

def form(request):
    context = {}
    return render(request, 'form.html', context)


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def depatments(request):
    return render(request, 'depatments.html')


def doctor(request):
    return render(request, 'doctor.html')


def gettemp(request):
    global g_messageJson
    ict0 = json.loads(g_messageJson)
    return JsonResponse(ict0)  # 放字典类型数据