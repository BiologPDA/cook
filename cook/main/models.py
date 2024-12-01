from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import User
from django.conf import settings 

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username

class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category_choices = [ 
        ('starter', 'Закуски'),
        ('main', 'Основные блюда'),
        ('dessert', 'Десерты'),
        ('drink', 'Напитки')
    ]
    category = models.CharField(max_length=50, choices=category_choices)
    image = models.ImageField(upload_to='dishes/', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  
    product = models.CharField(max_length=255, default='')  
    quantity = models.IntegerField(default=1)  
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    status = models.CharField(max_length=50, choices=[('pending', 'Ожидает'), ('completed', 'Завершен')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Заказ #{self.id} для {self.user.username}"

class Reservation(models.Model):
    customer_name = models.CharField(max_length=255) 
    date = models.DateTimeField()  # Дата и время бронирования , вместе, мне просто понравалось как выглядит выпадашка
    number_of_people = models.PositiveIntegerField()  
    duration = models.PositiveIntegerField() 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Кастомный пользователь

    def __str__(self):
        return f'Бронирование от {self.customer_name} на {self.date}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

class Employee(models.Model):
    ROLE_CHOICES = [
        ('chef', 'Повар'),
        ('waiter', 'Официант'),
        ('manager', 'Менеджер')
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE) 
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

class Review(models.Model):
    customer_name = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer_name} - {self.rating}"

class Discount(models.Model):
    code = models.CharField(max_length=255)
    discount_percentage = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Discount: {self.code} ({self.discount_percentage}%)"

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
