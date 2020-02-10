from django.shortcuts import render
from django.http import HttpResponse


def quiz(request):
    return render(request, 'question.html')
