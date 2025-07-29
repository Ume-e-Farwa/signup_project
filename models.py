from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=150, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    posts_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username

class Post(models.Model):
    username = models.CharField(max_length=100 , default="Anonymous")
    description = models.TextField(default="No description available")  # Add a default value
    image = models.ImageField(upload_to='explore_images/')



class Reel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='reels/')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

