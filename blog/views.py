from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Q
from django.contrib import messages

from .forms import RegisterForm, LoginForm, ResourceForm, PostForm, CommentForm
from .models import Resource, Post, Comment


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# -----------------------------
# RESOURCES
# -----------------------------
def resources(request):
    resources_qs = Resource.objects.all()

    if not request.user.is_staff:
        resources_qs = resources_qs.filter(is_approved=True)

    subject = request.GET.get("subject")
    year = request.GET.get("year")
    query = request.GET.get("q")

    if subject:
        resources_qs = resources_qs.filter(subject=subject)

    if year:
        resources_qs = resources_qs.filter(year_group=year)

    if query:
        resources_qs = resources_qs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, "resources.html", {
        "resources": resources_qs,
        "selected_subject": subject,
        "selected_year": year,
        "query": query,
    })


@login_required
def upload_resource(request):
    form = ResourceForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        resource = form.save(commit=False)
        resource.uploaded_by = request.user
        resource.is_approved = False
        resource.save()
        messages.success(request, "Resource uploaded successfully and is awaiting approval.")
        return redirect("resources")

    return render(request, "upload.html", {"form": form})


@login_required
def edit_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    if resource.uploaded_by != request.user and not request.user.is_staff:
        return HttpResponseForbidden("Not allowed.")

    form = ResourceForm(request.POST or None, request.FILES or None, instance=resource)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Resource updated successfully.")
        return redirect("resources")

    return render(request, "edit_resource.html", {"form": form, "resource": resource})


@login_required
def delete_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    if resource.uploaded_by != request.user and not request.user.is_staff:
        return HttpResponseForbidden("Not allowed.")

    if request.method == "POST":
        resource.delete()
        messages.success(request, "Resource deleted successfully.")
        return redirect("resources")

    return render(request, "confirm_delete.html", {"resource": resource})


def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    if not resource.is_approved and not request.user.is_staff:
        return HttpResponseForbidden("Pending approval.")

    approved_comments = resource.comments.filter(is_approved=True)

    my_pending_comments = Comment.objects.none()
    if request.user.is_authenticated:
        my_pending_comments = resource.comments.filter(author=request.user, is_approved=False)

    form = CommentForm()

    return render(request, "resource_detail.html", {
        "resource": resource,
        "comments": approved_comments,
        "my_pending_comments": my_pending_comments,
        "form": form,
    })


@login_required
def add_resource_comment(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.resource = resource
            comment.is_approved = False
            comment.save()
            messages.success(request, "Your comment has been submitted and is awaiting admin approval.")

    return redirect("resource_detail", pk=resource_id)


# -----------------------------
# POSTS
# -----------------------------
def posts(request):
    posts_qs = Post.objects.all()

    if not request.user.is_staff:
        posts_qs = posts_qs.filter(is_approved=True)

    return render(request, "posts.html", {"posts": posts_qs})


@login_required
def create_post(request):
    form = PostForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.is_approved = False
        post.save()
        messages.success(request, "Post created and is awaiting approval.")
        return redirect("posts")

    return render(request, "create_post.html", {"form": form})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("Not allowed.")

    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Post updated successfully.")
        return redirect("posts")

    return render(request, "edit_post.html", {"form": form, "post": post})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("Not allowed.")

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect("posts")

    return render(request, "confirm_delete_post.html", {"post": post})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if not post.is_approved and not request.user.is_staff:
        return HttpResponseForbidden("Pending approval.")

    approved_comments = post.comments.filter(is_approved=True)

    my_pending_comments = Comment.objects.none()
    if request.user.is_authenticated:
        my_pending_comments = post.comments.filter(author=request.user, is_approved=False)

    form = CommentForm()

    return render(request, "post_detail.html", {
        "post": post,
        "comments": approved_comments,
        "my_pending_comments": my_pending_comments,
        "form": form,
    })


@login_required
def add_post_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.is_approved = False
            comment.save()
            messages.success(request, "Your comment has been submitted and is awaiting admin approval.")

    return redirect("post_detail", pk=post_id)


# -----------------------------
# AUTH
# -----------------------------
def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "auth/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.cleaned_data["user"])
        return redirect("home")

    return render(request, "auth/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")