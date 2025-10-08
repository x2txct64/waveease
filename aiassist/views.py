from django.shortcuts import render

# Create your views here.

def lesson(request):
    return render(request, "aiassist/lesson.html")

def rubric(request):
    return render(request, "aiassist/rubric.html")

def quiz(request):
    return render(request, "aiassist/quiz.html")

def email(request):
    return render(request, "aiassist/email.html")