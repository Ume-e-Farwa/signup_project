from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Post

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'profile_pic', 'followers_count', 'following_count', 'posts_count']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['username', 'description', 'image']
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

