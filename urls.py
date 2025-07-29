from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
      path('explore/', views.explore_page, name='explore'),
       path('index', views.index, name='index'),
    path('home/', views.home, name='home'),
       path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/list/', views.post_list, name='post_list'),
    path('post/update/<int:pk>/', views.post_update, name='post_update'),
    path('post/delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('register-step1/', views.register_step1, name='register-step1'),
    path('register-step2/', views.register_step2, name='register-step2'),
    path('register step-3/', views.register_step3, name='register step-3'),
    path('register-step4/', views.register_step4, name='register-step4'),
    path('register-step5/', views.register_step5, name='register-step5'),
]
 