from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("resources/", views.resources, name="resources"),
    path("posts/", views.posts, name="posts"),
    path("about/", views.about, name="about"),

    # auth
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # resource management
    path("upload/", views.upload_resource, name="upload_resource"),

    # resource editing/deletion
    path("resources/<int:pk>/edit/", views.edit_resource, name="edit_resource"),
    path("resources/<int:pk>/delete/", views.delete_resource, name="delete_resource"),

    # post management
    path("posts/create/", views.create_post, name="create_post"),
    path("posts/<int:pk>/edit/", views.edit_post, name="edit_post"),
    path("posts/<int:pk>/delete/", views.delete_post, name="delete_post")
]
