from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Импортируем нашу кастомную модель

class UserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text="Введите ваш номер телефона.")
    
    # Удаляем email поле, чтобы оно не показывалось
    email = None

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'password1', 'password2']
