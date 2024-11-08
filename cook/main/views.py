from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login
from .models import Order


def index(request):
    return render(request, 'main/index.html')

def menu(request):
    return render(request, 'main/menu.html')

def about(request):
    return render(request, 'main/about.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def reservation(request):
    return render(request, 'main/reservation.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем пользователя
            login(request, user)  # Логиним пользователя
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def dishes(request):
    return render(request, 'main/dishes.html')

def main_dish(request):
    return render(request, 'main/main_dish.html')

def desserts(request):
    return render(request, 'main/desserts.html')

def bar(request):
    return render(request, 'main/bar.html')

def admin_view(request):
    if not request.user.is_staff:
        return redirect('home')
    return render(request, 'admin_dashboard.html')

def profile_view(request):
    # Получаем все заказы для текущего пользователя
    orders = Order.objects.filter(user=request.user)
    
    # Передаем заказы в шаблон
    return render(request, 'main/profile.html', {'orders': orders})