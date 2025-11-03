from django.urls import path
from . import views

app_name = "aiassist"

urlpatterns = [
    path("lesson-planner/", views.lesson_planner_view, name = "lesson"),
    path("rubric/", views.rubric_maker_view, name = "rubric"),
    path("quiz/", views.quiz_maker_view, name ="quiz"),
    path("email/", views.email_framer_view, name ="email"),
    path("grade/", views.grading_assistant_view, name ="grade"),
    path("level/", views.text_leveler_view, name ="level"),
]