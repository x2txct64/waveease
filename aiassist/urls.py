from django.urls import path
from . import views

app_name = "aiassist"

urlpatterns = [
    path("lesson-planner/", views.lesson_planner_view, name = "lesson"),
    path("rubric/", views.rubric, name = "rubric"),
    path("quiz/", views.quiz, name ="quiz"),
    path("email/", views.email, name ="email"),
    path("grade/", views.grade, name ="grade"),
    path("level/", views.level, name ="level"),
]