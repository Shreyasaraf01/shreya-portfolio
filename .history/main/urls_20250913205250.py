from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("career/", views.career, name="career"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),
]
