from django.db import models
from django.contrib.auth.models import AbstractUser  # Импортируем AbstractUser для кастомной модели пользователя

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)  # Поле для номера телефона

    # Отключаем использование поля email
    email = None  # Не используем поле email

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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)  # Присваиваем дефолтного пользователя с ID 1
    product = models.CharField(max_length=255, default='')  # Название продукта или описание заказа, дефолтное значение
    quantity = models.IntegerField(default=1)  # Количество с дефолтным значением
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Цена с дефолтным значением
    status = models.CharField(max_length=50, choices=[('pending', 'Ожидает'), ('completed', 'Завершен')], default='pending')  # Статус заказа с дефолтным значением
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return f"Заказ #{self.id} для {self.user.username}"

class Reservation(models.Model):
    customer_name = models.CharField(max_length=255)
    date = models.DateTimeField()
    number_of_people = models.PositiveIntegerField()
    status_choices = [
        ('confirmed', 'Подтверждено'),
        ('pending', 'Ожидает'),
        ('canceled', 'Отменено')
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return f"Reservation {self.id} - {self.customer_name}"

class Employee(models.Model):
    ROLE_CHOICES = [
        ('chef', 'Повар'),
        ('waiter', 'Официант'),
        ('manager', 'Менеджер')
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Используем CustomUser вместо User
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Используем CustomUser вместо User
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
