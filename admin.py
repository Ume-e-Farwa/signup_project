from django.contrib import admin
# from .models import Profile, Post
# admin.site.register(Profile)
# admin.site.register(Post)
class ProfileAdmin(admin.ModelAdmin):
 list_display = ('user', 'bio', 'created_at')
search_fields = ('user__username', 'bio')
 