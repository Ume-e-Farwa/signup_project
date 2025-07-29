from cProfile import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, ProfileForm, PostForm, LoginForm
from .models import UserProfile, Post

# Index View
def index(request):
    return render(request, 'index.html')

# Logout View
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Create a UserProfile instance for the new user
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})


def explore_page(request):
    posts = Post.objects.all()
    return render(request, 'explore.html', {'posts': posts})


# CRUD for Posts
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})

# Home View
def home(request):
    return render(request, 'home.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
# register_step1 view
def register_step1(request):
    return render(request, 'register-step1.html')
# register_step2 view
def register_step2(request):
    return render(request, 'register-step2.html')
# register_step3 view
def register_step3(request):
    return render(request, 'register step-3.html')
# register_step4 view
def register_step4(request):
    return render(request, 'register-step4.html')
# register_step5 view
def register_step5(request):
    return render(request, 'register-step5.html')