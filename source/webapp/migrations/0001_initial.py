# Generated by Django 2.2 on 2019-09-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('mail', models.EmailField(max_length=254, verbose_name='Почта автора')),
                ('feedback_text', models.TextField(max_length=2000, verbose_name='Текст записи')),
                ('first_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('second_time', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=50, verbose_name='Статус')),
            ],
        ),
    ]