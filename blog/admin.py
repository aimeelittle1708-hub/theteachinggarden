from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils import timezone

from .models import User, Resource, Post, Comment


# ----------------------
# Custom User Admin
# ----------------------
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ("email",)
    list_display = ("email", "name", "is_staff", "is_active", "is_superuser")
    search_fields = ("email", "name")
    list_filter = ("is_staff", "is_active", "is_superuser")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("name",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")


# ----------------------
# Resource Admin
# ----------------------
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "year_group", "uploaded_by", "is_approved", "created_at")
    list_filter = ("subject", "year_group", "is_approved", "created_at")
    search_fields = ("title", "description", "uploaded_by__email")
    actions = ["approve_resources", "hide_resources"]

    def approve_resources(self, request, queryset):
        queryset.update(is_approved=True, approved_by=request.user, approved_at=timezone.now())
    approve_resources.short_description = "Approve selected resources"

    def hide_resources(self, request, queryset):
        queryset.update(is_approved=False)
    hide_resources.short_description = "Hide selected resources"


# ----------------------
# Comment Inline on Posts
# ----------------------
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ("author", "content", "is_approved", "created_at")
    readonly_fields = ("created_at",)


# ----------------------
# Post Admin
# ----------------------
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_approved", "created_at")
    list_filter = ("is_approved", "created_at")
    search_fields = ("title", "content", "author__email")
    actions = ["approve_posts", "hide_posts"]

    def approve_posts(self, request, queryset):
        queryset.update(is_approved=True, approved_by=request.user, approved_at=timezone.now())
    approve_posts.short_description = "Approve selected posts"

    def hide_posts(self, request, queryset):
        queryset.update(is_approved=False)
    hide_posts.short_description = "Hide selected posts"


# ----------------------
# Comment Admin (Moderation)
# ----------------------
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "is_approved", "created_at")
    list_filter = ("is_approved", "created_at")
    search_fields = ("content", "author__email", "post__title")
    actions = ["approve_comments", "hide_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True, approved_by=request.user, approved_at=timezone.now())
    approve_comments.short_description = "Approve selected comments"

    def hide_comments(self, request, queryset):
        queryset.update(is_approved=False)
    hide_comments.short_description = "Hide selected comments"