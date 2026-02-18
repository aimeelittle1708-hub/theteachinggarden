from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Post, Comment, Resource, Subject, SubSubject
from .forms import PostForm, CommentForm, ResourceForm
from django.contrib.auth.models import User

# ===== Post Views =====

def post_list(request):
    """Display all published posts with pagination (3 per row, 6 per page)"""
    posts = Post.objects.filter(status=1).order_by('-id')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, id):
    """Display a single post with comments"""
    post = get_object_or_404(Post, id=id, status=1)
    comments = Comment.objects.filter(post_id=post).order_by('-created_on')
    resources = Resource.objects.filter(post_id=post)
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user_id = request.user
                comment.post_id = post
                comment.save()
                messages.success(request, 'Comment added successfully!')
                return redirect('post_detail', id=post.id)
        else:
            messages.error(request, 'You must be logged in to comment.')
            return redirect('login')
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'resources': resources,
        'form': form,
    }
    return render(request, 'blog/post_detail.html', context)


@login_required(login_url='login')
def post_create(request):
    """Create a new post"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)


@login_required(login_url='login')
def post_edit(request, id):
    """Edit an existing post"""
    post = get_object_or_404(Post, id=id)
    
    # Check if user owns the post
    if post.user_id != request.user:
        messages.error(request, 'You can only edit your own posts!')
        return redirect('post_detail', id=post.id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    
    context = {'form': form, 'post': post}
    return render(request, 'blog/post_form.html', context)


@login_required(login_url='login')
def post_delete(request, id):
    """Delete a post"""
    post = get_object_or_404(Post, id=id)
    
    # Check if user owns the post
    if post.user_id != request.user:
        messages.error(request, 'You can only delete your own posts!')
        return redirect('post_detail', id=post.id)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('post_list')
    
    context = {'post': post}
    return render(request, 'blog/post_confirm_delete.html', context)


# ===== Resource Views =====

def resource_list(request):
    """Display all resources with pagination"""
    resources = Resource.objects.all().order_by('-created_on')
    paginator = Paginator(resources, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'resources': page_obj.object_list,
    }
    return render(request, 'blog/resource_list.html', context)


# ===== Authentication Views =====

def register(request):
    """User registration"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created! Please log in.')
        return redirect('login')
    
    return render(request, 'blog/register.html')


def user_login(request):
    """User login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('post_list')
        else:
            messages.error(request, 'Invalid username or password!')
    
    return render(request, 'blog/login.html')


def user_logout(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('post_list')


# ===== Contact View =====

def contact(request):
    """Contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('post_list')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'blog/contact.html', context)
