import time

from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, "clock/index.html")


def current_time(request):
    now = time.localtime()
    return JsonResponse(
        {
            "date": time.strftime("%A, %D %B %Y", now),
            "time": time.strftime("%H:%M:%S", now),
        }
    )
