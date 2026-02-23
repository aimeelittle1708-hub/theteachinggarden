from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Q

from .forms import RegisterForm, LoginForm, ResourceForm, PostForm
from .models import Resource, Post


def home(request):
    return render(request, "home.html")


def resources(request):
    resources_qs = Resource.objects.all()

    # Normal users only see approved resources.
    # Staff/superusers can see everything.
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

    context = {
        "resources": resources_qs,
        "selected_subject": subject,
        "selected_year": year,
        "query": query,
    }
    return render(request, "resources.html", context)


def posts(request):
    posts_qs = Post.objects.all()

    # Normal users only see approved posts.
    # Staff/superusers can see everything.
    if not request.user.is_staff:
        posts_qs = posts_qs.filter(is_approved=True)

    return render(request, "posts.html", {"posts": posts_qs})


def about(request):
    return render(request, "about.html")


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


@login_required
def upload_resource(request):
    form = ResourceForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        resource = form.save(commit=False)
        resource.uploaded_by = request.user

        # New uploads are pending until admin approves
        resource.is_approved = False
        resource.approved_by = None
        resource.approved_at = None

        resource.save()
        return redirect("resources")

    return render(request, "upload.html", {"form": form})


@login_required
def edit_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    # Owner OR staff can edit
    if resource.uploaded_by != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to edit this resource.")

    form = ResourceForm(request.POST or None, request.FILES or None, instance=resource)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("resources")

    return render(request, "edit_resource.html", {"form": form, "resource": resource})


@login_required
def delete_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    # Owner OR staff can delete
    if resource.uploaded_by != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to delete this resource.")

    if request.method == "POST":
        # Try to delete the Cloudinary asset too
        try:
            resource.file.delete()
        except Exception:
            pass

        resource.delete()
        return redirect("resources")

    return render(request, "confirm_delete.html", {"resource": resource})


@login_required
def create_post(request):
    form = PostForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user

        # If you want posts to be approved by admin first:
        post.is_approved = False
        post.approved_by = None
        post.approved_at = None

        post.save()
        return redirect("posts")

    return render(request, "create_post.html", {"form": form})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Owner OR staff can edit
    if post.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You cannot edit this post.")

    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("posts")

    return render(request, "edit_post.html", {"form": form, "post": post})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Owner OR staff can delete
    if post.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("You cannot delete this post.")

    if request.method == "POST":
        post.delete()
        return redirect("posts")

    return render(request, "confirm_delete_post.html", {"post": post})