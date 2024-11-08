from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from main import views

def home(request):
    return redirect('home') 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),  # Пути для приложения main
    path('', views.index, name='index'),  # Главная страница
    path('main/', include('main.urls')),  # Пути для страниц аутентификации
    path('', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)