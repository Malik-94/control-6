from django.db import models

STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
]


class Book(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя автора')
    mail = models.EmailField(verbose_name='Почта автора')
    feedback_text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст записи')
    first_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    second_time = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=50, null=False, blank=False, choices=STATUS_CHOICES, default='active',
                              verbose_name='Статус')

    def __str__(self):
        return self.name
