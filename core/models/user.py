from django.db import models


# Create your models here.
class User(models.Model):
    fio = models.CharField(max_length=50, verbose_name="ФИО", blank=True)
    email = models.EmailField(max_length=100, verbose_name="Email", blank=True)
    password = models.CharField(max_length=100, verbose_name="Пароль", blank=True)
    active = models.BooleanField(max_length=1, verbose_name="Активность", blank=True)
    last_visit = models.DateTimeField(verbose_name="Дата последнего визита", blank=True)

    def __str__(self):
        return self.fio

    class Meta:
        ordering = ['fio']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


