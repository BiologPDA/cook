from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Главная страница
    path('home/', views.index, name='home'),  

    # Меню
    path('menu/', views.menu, name='menu'),  

    # О нас
    path('about/', views.about, name='about'),  

    # Галерея
    path('gallery/', views.gallery, name='gallery'),  

    # Контакты
    path('contacts/', views.contacts, name='contacts'),  

    # Бронирование
    path('reservation/', views.reservation_view, name='reservation'),

    # Вход
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),

    # Выход (можно использовать стандартный или ваш кастомный)
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_view, name='logout'),  # Страница выхода

    # Регистрация
    path('register/', views.register, name='register'),
    # Блюда
    path('dishes/', views.dishes, name='dishes'),

    # Основные блюда
    path('main_dish/', views.main_dish, name='main_dish'),

    # Бар
    path('bar/', views.bar, name='bar'),

    # Десерты
    path('desserts/', views.desserts, name='desserts'),

    # Профиль
    path('profile/', views.profile_view, name='profile'),
    path('', views.home_view, name='home'),
    path('', views.index, name='index'),

]
