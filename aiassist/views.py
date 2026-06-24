from django.shortcuts import render
from .ai_utils import generate_ai_response, extract_text
import markdown

MARKDOWN_CONFIG = {
    "extensions": ["pymdownx.arithmatex"],
    "extension_configs": {
        "pymdownx.arithmatex": {"generic": True}
    }
}


def _process_ai_request(request, prompt_type, template_name, fields):
    result = None
    if request.method == "POST":
        uploaded_file = request.FILES.get('materials')
        uploaded_text = extract_text(uploaded_file) if uploaded_file else ""

        user_input = "\n".join(
            f"{label}: {request.POST.get(field_name, '')}"
            for field_name, label in fields.items()
        )
        user_input += f"\nUpload Materials: {uploaded_text}"

        if user_input.strip():
            result = markdown.markdown(
                generate_ai_response(prompt_type, user_input),
                **MARKDOWN_CONFIG
            )
    return render(request, template_name, {"result": result})


def lesson_planner_view(request):
    fields = {
        "subject": "Subject",
        "topic": "Topic",
        "objectives": "Objectives",
        "activities": "Activities",
        "assessment": "Assessment",
        "less-dur": "Lesson Duration",
    }
    return _process_ai_request(request, "lesson_planner", "aiassist/lesson.html", fields)


def rubric_maker_view(request):
    fields = {
        "subject": "Subject",
        "topic": "Topic",
        "activity": "Activity",
        "categories": "Rubric Categories",
    }
    return _process_ai_request(request, "rubric_maker", "aiassist/rubric.html", fields)


def quiz_maker_view(request):
    fields = {
        "subject": "Subject",
        "topic": "Topic",
        "amount": "Amount Of Questions",
        "difficulty": "Quiz Difficulty",
    }
    return _process_ai_request(request, "quiz_maker", "aiassist/quiz.html", fields)


def email_framer_view(request):
    fields = {
        "topic": "Topic",
        "addressed": "Who is it addressed to",
        "formal": "How Formal",
        "info": "Additional Information",
    }
    return _process_ai_request(request, "email_framer", "aiassist/email.html", fields)


def grading_assistant_view(request):
    fields = {
        "subject": "Subject",
        "topic": "Topic",
        "assignment": "Type Of Assignment",
        "objective": "Learning Objective",
        "question": "Test Question",
        "text": "Student Text",
    }
    return _process_ai_request(request, "grading_assistant", "aiassist/grade.html", fields)


def text_leveler_view(request):
    fields = {
        "grade": "Grade Level",
        "focus": "Focus Point",
    }
    return _process_ai_request(request, "text_leveler", "aiassist/level.html", fields) 