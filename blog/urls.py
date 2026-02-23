from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Resources
    path("resources/", views.resources, name="resources"),
    path("resources/<int:pk>/", views.resource_detail, name="resource_detail"),
    path("resources/<int:resource_id>/comment/", views.add_resource_comment, name="add_resource_comment"),

    # Posts
    path("posts/", views.posts, name="posts"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("posts/<int:post_id>/comment/", views.add_post_comment, name="add_post_comment"),

    # About
    path("about/", views.about, name="about"),

    # Auth
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Resource management
    path("upload/", views.upload_resource, name="upload_resource"),
    path("resources/<int:pk>/edit/", views.edit_resource, name="edit_resource"),
    path("resources/<int:pk>/delete/", views.delete_resource, name="delete_resource"),

    # Post management
    path("posts/create/", views.create_post, name="create_post"),
    path("posts/<int:pk>/edit/", views.edit_post, name="edit_post"),
    path("posts/<int:pk>/delete/", views.delete_post, name="delete_post"),

    # Comment management
    path("comments/<int:pk>/edit/", views.edit_comment, name="edit_comment"),
    path("comments/<int:pk>/delete/", views.delete_comment, name="delete_comment"),
]