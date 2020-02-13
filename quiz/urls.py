from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.quiz, name="quiz-view"),
    path('check', views.check_answer, name="check-view"),
]
