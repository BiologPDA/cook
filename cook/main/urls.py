from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('menu', views.menu, name='menu'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('contacts', views.contacts, name='contacts'),
    path('reservation', views.reservation, name='reservation'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),  # Страница входа
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Страница выхода
    path('register/', views.register, name='register'),  # Страница регистрации
    path('dishes', views.dishes, name='dishes'),
    path('main_dish', views.main_dish, name='main_dish'),
    path('bar', views.bar, name='bar'),
    path('desserts', views.desserts, name='desserts'),
    path('profile/', views.profile_view, name='profile'),
]
