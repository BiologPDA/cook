from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import UserRegistrationForm,ReservationForm
from .models import Reservation,Order



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

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            success_message = "Ваше бронирование успешно!"
            return render(request, 'main/reservation.html', {'form': form, 'success_message': success_message})
    else:
        form = ReservationForm(initial={'user': request.user.id})
    
    return render(request, 'main/reservation.html', {'form': form})
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт успешно создан! Вы можете войти.')
            return redirect('index') 
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
    orders = Order.objects.filter(user=request.user)
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'main/profile.html', {'orders': orders, 'reservations': reservations})


def logout_view(request):
    logout(request)  # Завершаем сессию пользователя
    return redirect('home')  # Перенаправляем на главную страницу

def home_view(request):
    return render(request, 'main/index.html')

