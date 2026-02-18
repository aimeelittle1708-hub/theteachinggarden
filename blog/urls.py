from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("resources/", views.resources, name="resources"),
    path("posts/", views.posts, name="posts"),
    path("about/", views.about, name="about"),
]
