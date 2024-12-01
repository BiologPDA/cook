from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reservation, CustomUser

# Форма регистрации пользователя
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'phone_number', 'password1', 'password2']
        
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'date', 'number_of_people', 'duration', 'user']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'user': forms.HiddenInput(),  # скрытое поле для пользователя
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].initial = kwargs.get('initial', {}).get('user')