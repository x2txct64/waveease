from django.shortcuts import render
from .ai_utils import generate_ai_response

# Create your views here.

def lesson(request):
    return render(request, "aiassist/lesson.html")

def rubric(request):
    return render(request, "aiassist/rubric.html")

def quiz(request):
    return render(request, "aiassist/quiz.html")

def email(request):
    return render(request, "aiassist/email.html")

def grade(request):
    return render(request, "aiassist/grade.html")

def level(request):
    return render(request, "aiassist/level.html")

def lesson_planner_view(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("lesson_input", "")
        if user_input:
            result = generate_ai_response("lesson_planner", user_input)
    return render(request, "lesson_planner.html", {"result": result})


def rubric_maker_view(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("rubric_input", "")
        if user_input:
            result = generate_ai_response("rubric_maker", user_input)
    return render(request, "rubric_maker.html", {"result": result})


def quiz_maker_view(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("quiz_input", "")
        if user_input:
            result = generate_ai_response("quiz_maker", user_input)
    return render(request, "quiz_maker.html", {"result": result})


def email_framer_view(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("email_input", "")
        if user_input:
            result = generate_ai_response("email_framer", user_input)
    return render(request, "email_framer.html", {"result": result})


def grading_assistant_view(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("grading_input", "")
        if user_input:
            result = generate_ai_response("grading_assistant", user_input)
    return render(request, "grading_assistant.html", {"result": result})


def text_leveler_view(request):
    result = None
    if request.method == "POST":
        user_input = request.POST.get("level_input", "")
        if user_input:
            result = generate_ai_response("text_leveler", user_input)
    return render(request, "text_leveler.html", {"result": result})