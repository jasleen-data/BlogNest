from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .models import Post, Category


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)
        return redirect('home')

    return render(request, 'blog/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(
            request=request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'blog/login.html')

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('home')


@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        category_name = request.POST['category']
        content = request.POST['content']

        category, created = Category.objects.get_or_create(
            name=category_name
        )

        Post.objects.create(
            title=title,
            category=category,
            content=content,
            author=request.user
        )

        messages.success(request, 'Post created successfully!')
        return redirect('home')

    return render(request, 'blog/create_post.html')


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']

        category_name = request.POST.get(
            'category',
            post.category.name if post.category else ''
        )

        if category_name:
            category, created = Category.objects.get_or_create(
                name=category_name
            )
            post.category = category

        post.save()

        messages.success(request, 'Post updated successfully!')
        return redirect('post_detail', post_id=post.id)

    return render(
        request,
        'blog/edit_post.html',
        {'post': post}
    )


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )

    if request.method == 'POST':
        post.delete()

        messages.success(
            request,
            'Post deleted successfully!'
        )

        return redirect('home')

    return render(
        request,
        'blog/delete_post.html',
        {'post': post}
    )