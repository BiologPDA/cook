from django.contrib import admin
from .models import Dish, Order
from django.db.models import Sum

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    search_fields = ('name', 'category')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price', 'total_price', 'status', 'created_at')  # Используем user вместо customer_name
    list_filter = ('status',)
    search_fields = ('user__username',)  # Поиск по имени пользователя
    actions = ['generate_report']

    def total_price(self, obj):
        return obj.quantity * obj.price  # Рассчитываем общую цену
    total_price.admin_order_field = 'price'  # Для сортировки по общей цене
    total_price.short_description = 'Total Price'  # Описание колонки

    def generate_report(self, request, queryset):
        # Пример отчета: общая сумма заказов
        total_revenue = queryset.aggregate(Sum('total_price'))['total_price__sum']
        self.message_user(request, f'Total revenue: {total_revenue}')
    generate_report.short_description = "Генерировать отчет"
