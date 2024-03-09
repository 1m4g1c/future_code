from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("aboutme", views.aboutme, name="aboutme"),
    path("new_comment", views.new_comment, name="new_comment")
]

