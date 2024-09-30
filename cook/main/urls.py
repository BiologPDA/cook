
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='home'),
path('menu', views.menu, name='menu'),
path('about', views.about, name='about'),
path('gallery', views.gallery, name='gallery'),
path('contacts', views.contacts, name='contacts'),
path('reservation', views.reservation, name='reservation'),
path('login', views.login, name='login'),
path('register', views.register, name='register')
]
