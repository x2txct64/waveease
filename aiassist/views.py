from django.shortcuts import render
from .ai_utils import generate_ai_response
import markdown

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
        user_input = f"""
        Grade Level: {request.POST.get('grade', '')}
        Topic: {request.POST.get('topic', '')}
        Objectives: {request.POST.get('objectives', '')}
        Activities: {request.POST.get('activities', '')}
        Assessment: {request.POST.get('assessment', '')}
        Lesson Duration: {request.POST.get('less-dur', '')}
        Upload Materials: (skip for testing)
        """

        if user_input:
            result = markdown.markdown(generate_ai_response("lesson_planner", user_input))
    return render(request, "aiassist/lesson.html", {"result": result})


def rubric_maker_view(request):
    result = None
    if request.method == "POST":
        user_input = f"""
        Grade Level: {request.POST.get('grade', '')}
        Topic: {request.POST.get('topic', '')}
        Objectives: {request.POST.get('objectives') }
        Rubric Catagories: {request.POST.get('catagories', '')}
        Upload Materials: (skip for testing)
        """
        if user_input:
            result = markdown.markdown(generate_ai_response("rubric_maker", user_input))
    return render(request, "aiassist/rubric.html", {"result": result})


def quiz_maker_view(request):
    result = None
    if request.method == "POST":
        user_input =f"""
        Grade Level: {request.POST.get('grade', '')}
        Topic: {request.POST.get('topic', '')}
        Amount Of Questions: {request.POST.get('amount', '')}
        Question type: {request.POST.get('question', '')}
        Quiz Timer: {request.POST.get('type', '')}
        Upload Materials: (skip for testing)
        """
        if user_input:
            result = generate_ai_response("quiz_maker", user_input)
    return render(request, "aiassist/quiz.html", {"result": result})


def email_framer_view(request):
    result = None
    if request.method == "POST":
        user_input =f""" 
        Topic: {request.POST.get('topic', '')}
        Who is it addressed to: {request.POST.get('addressed', '')}
        How Formal: {request.POST.get('formal', '')}
        Additional Information: {request.POST.get('info', '')}
        Upload Materials: (skip for testing)
        """
        if user_input:
            result = generate_ai_response("email_framer", user_input)
    return render(request, "aiassist/email.html", {"result": result})


def grading_assistant_view(request):
    result = None
    if request.method == "POST":
        user_input =f"""
        Grade Level: {request.POST.get('grade', '')}
        Topic: {request.POST.get('topic', '')}
        Type Of Assignment: {request.POST.get('assignment', '')}
        Learning Objective: {request.POST.get('objective', '')}
        Required Elements: {request.POST.get('elements', '')}
        Student Text: {request.POST.get('elements', '')}
        Upload Materials: (skip for testing)
        """
        if user_input:
            result = generate_ai_response("grading_assistant", user_input)
    return render(request, "aiassist/grading_assistant.html", {"result": result})


def text_leveler_view(request):
    result = None
    if request.method == "POST":
        user_input =f"""
        Grade Level: {request.POST.get('grade', '')}
        Focus Point: {request.POST.get('focus', '')}
        Text Length: {request.POST.get('length', '')}
        Input Length: {request.POST.get('Input Text', '')}
        Upload Materials: (skip for testing)
        """
        if user_input:
            result = generate_ai_response("text_leveler", user_input)
    return render(request, "aiassist/text_leveler.html", {"result": result})