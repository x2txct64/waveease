from django.shortcuts import render
from .ai_utils import generate_ai_response
import markdown
from django.core.files.storage import FileSystemStorage
from .ai_utils import extract_text


# Create your views here.


# Gets each input of user and print ai response in markdown
def lesson_planner_view(request):
    result = None
    if request.method == "POST":
        uploaded_file = request.FILES.get('materials')
        uploaded_text = extract_text(uploaded_file)

        user_input = f"""
        Subject: {request.POST.get('subject', '')}
        Topic: {request.POST.get('topic', '')}
        Objectives: {request.POST.get('objectives', '')}
        Activities: {request.POST.get('activities', '')}
        Assessment: {request.POST.get('assessment', '')}
        Lesson Duration: {request.POST.get('less-dur', '')}
        Upload Materials: {uploaded_text}
        """

        if user_input.strip():
            result = markdown.markdown(
                generate_ai_response("lesson_planner", user_input),
                extensions=["pymdownx.arithmatex"],
                extension_configs={
                    "pymdownx.arithmatex": {
                        "generic": True
            }
        }
                )
    return render(request, "aiassist/lesson.html", {"result": result})


def rubric_maker_view(request):
    result = None
    if request.method == "POST":
        uploaded_file = request.FILES.get('materials')
        uploaded_text = extract_text(uploaded_file)

        user_input = f"""
        Subject: {request.POST.get('subject', '')}
        Topic: {request.POST.get('topic', '')}
        Objectives: {request.POST.get('objectives') }
        Activitity: {request.POST.get('activity', '')}
        Rubric Catagories: {request.POST.get('catagories', '')}
        Upload Materials: {uploaded_text}
        """
        if user_input.strip():
            result = markdown.markdown(
                generate_ai_response("rubric_maker", user_input),
                extensions=["pymdownx.arithmatex"],
                extension_configs={
                    "pymdownx.arithmatex": {
                        "generic": True
            }
        }
                )
    return render(request, "aiassist/rubric.html", {"result": result})


def quiz_maker_view(request):
    result = None
    if request.method == "POST":
        uploaded_file = request.FILES.get('materials')
        uploaded_text = extract_text(uploaded_file)

        user_input =f"""
        Subject: {request.POST.get('subject', '')}
        Topic: {request.POST.get('topic', '')}
        Amount Of Questions: {request.POST.get('amount', '')}
        Quiz Difficulty: {request.POST.get('difficulty', '')}
        Upload Materials: {uploaded_text}
        """
        if user_input.strip():
            result =  markdown.markdown(
                generate_ai_response("quiz_maker", user_input),
                extensions=["pymdownx.arithmatex"],
                extension_configs={
                    "pymdownx.arithmatex": {
                        "generic": True
            }
        }
                )
    return render(request, "aiassist/quiz.html", {"result": result})


def email_framer_view(request):
    result = None
    if request.method == "POST":
        uploaded_file = request.FILES.get('materials')
        uploaded_text = extract_text(uploaded_file)

        user_input =f""" 
        Topic: {request.POST.get('topic', '')}
        Who is it addressed to: {request.POST.get('addressed', '')}
        How Formal: {request.POST.get('formal', '')}
        Additional Information: {request.POST.get('info', '')}
        Upload Materials: {uploaded_text}
        """
        if user_input.strip():
            result =  markdown.markdown(
                generate_ai_response("email_framer", user_input),
                extensions=["pymdownx.arithmatex"],
                extension_configs={
                    "pymdownx.arithmatex": {
                        "generic": True
            }
        }
                )
    return render(request, "aiassist/email.html", {"result": result})


def grading_assistant_view(request):
    result = None
    if request.method == "POST":
        uploaded_file = request.FILES.get('materials')
        uploaded_text = extract_text(uploaded_file)

        user_input =f"""
        Subject: {request.POST.get('subject', '')}
        Topic: {request.POST.get('topic', '')}
        Type Of Assignment: {request.POST.get('assignment', '')}
        Learning Objective: {request.POST.get('objective', '')}
        Test Question: {request.POST.get('question', '')}
        Student Text: {request.POST.get('text', '')}
        Upload Materials: {uploaded_text}
        """
        if user_input.strip():
            result =  markdown.markdown(
                generate_ai_response("grading_assistant", user_input),
                extensions=["pymdownx.arithmatex"],
                extension_configs={
                    "pymdownx.arithmatex": {
                        "generic": True
            }
        }
                )
    return render(request, "aiassist/grade.html", {"result": result})


def text_leveler_view(request):
    result = None
    if request.method == "POST":
        uploaded_file = request.FILES.get('materials')
        uploaded_text = extract_text(uploaded_file)

        user_input =f"""
        Grade Level: {request.POST.get('grade', '')}
        Focus Point: {request.POST.get('focus', '')}
        Input Text: {request.POST.get('input', '')}
        Upload Materials: {uploaded_text}
        """
        if user_input.strip():
            result =  markdown.markdown(
                generate_ai_response("text_leveler", user_input),
                extensions=["pymdownx.arithmatex"],
                extension_configs={
                    "pymdownx.arithmatex": {
                        "generic": True
            }
        }
                )
    return render(request, "aiassist/level.html", {"result": result}) 