from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import random


def quiz(request):
    questions = Question.objects.all()
    questions_list = list(questions)

    random.shuffle(questions_list)

    context = {
        "question": questions_list[0].content,
        "id": questions_list[0].id
    }
    return render(request, 'question.html', context)


def check_answer(request):
    given_id = request.POST.get('id', None)
    given_answer = request.POST.get('answer', None)

    correct_answer = Question.objects.filter(id=given_id).first().answer

    print(given_answer)
    print(correct_answer)
    if given_answer == correct_answer:
        status = "Odpowiedz poprawna"
    else:
        status = "Odpowiedz nieprawidlowa"

    return HttpResponse(status)
