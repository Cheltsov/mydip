from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import register

from core.models import User


class Goals(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)

    class Meta:
        db_table = 'goals'
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'


class NormalBodyParam(models.Model):
    height = models.FloatField(max_length=300, verbose_name="Рост", blank=True, null=True,
                               validators=[
                                   MaxValueValidator(300),
                                   MinValueValidator(1)
                               ])
    weight = models.FloatField(max_length=200, verbose_name="Вес", blank=True, null=True,
                               validators=[
                                   MaxValueValidator(200),
                                   MinValueValidator(1)
                               ])
    neck = models.FloatField(max_length=100, verbose_name="Шея", null=True)
    shoulders = models.FloatField(max_length=200, verbose_name="Плечи", null=True)
    chest_relax = models.FloatField(max_length=200, verbose_name="Грудь расслабленная", null=True)
    waist = models.FloatField(max_length=200, verbose_name="Талия", null=True)
    left_thigh = models.FloatField(max_length=100, verbose_name="Бедро левое", null=True)
    right_thigh = models.FloatField(max_length=100, verbose_name="Бедро правое", null=True)
    left_shin = models.FloatField(max_length=100, verbose_name="Голень левая", null=True)
    right_shin = models.FloatField(max_length=100, verbose_name="Голень правая", null=True)
    goal = models.ForeignKey(Goals, on_delete=models.DO_NOTHING)

    @register.filter(name='get_verbose_name')
    def get_verbose_name(self, name):
        return self._meta.get_field(name).verbose_name

    class Meta:
        db_table = 'normal_body_param'
        verbose_name = 'Нормальный параметр тела'
        verbose_name_plural = 'Нормальные параметры тела'


class UserGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goals, on_delete=models.DO_NOTHING)


class BodyExercise(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True)
    image = models.URLField(verbose_name='Картинка', null=True)
    category = models.CharField(max_length=250)
    main_muscles = models.TextField(verbose_name="Основные мышцы", null=True)
    minor_muscles = models.TextField(verbose_name="Второстепенные мышцы", null=True)
    sport_equipment = models.CharField(max_length=250, null=True)


class BodyWorkout(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    date_created = models.DateTimeField()
    date_finish = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    publications = models.ManyToManyField(BodyExercise)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goals, on_delete=models.CASCADE)


class UserFood(models.Model):
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', null=True)
    cal = models.IntegerField(verbose_name='Количество каллорий')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
