from django.urls import path
from . import views

app_name = "homepage"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("assist/", views.assist, name="assist"),
]