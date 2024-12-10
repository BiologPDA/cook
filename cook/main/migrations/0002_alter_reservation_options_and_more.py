# Generated by Django 5.1.3 on 2024-11-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'Бронирование', 'verbose_name_plural': 'Бронирования'},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='duration',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='number_of_people',
            field=models.PositiveIntegerField(),
        ),
    ]