import math

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.template.defaultfilters import register

from core.models import User


# Create your models here.
class UserExtSettings(models.Model):
    MAN = 'man'
    WOMAN = 'woman'
    CHOICES = (
        (MAN, 'Мужчина'),
        (WOMAN, 'Женщина'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=5, choices=CHOICES, default='MAN', null=True)
    age = models.IntegerField(verbose_name="Возраст", blank=True, default=1,
                              validators=[
                                  MaxValueValidator(120),
                                  MinValueValidator(1)
                              ])
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
    chest_tense = models.FloatField(max_length=200, verbose_name="Грудь напряженная", null=True)
    left_biceps_relax = models.FloatField(max_length=100, verbose_name="Левый бицепс расслабленный", null=True)
    right_biceps_relax = models.FloatField(max_length=100, verbose_name="Правый бицепс расслабленный", null=True)
    left_biceps_tense = models.FloatField(max_length=100, verbose_name="Левый бицепс напряженный", null=True)
    right_biceps_tense = models.FloatField(max_length=100, verbose_name="Правый бицепс напряженный", null=True)
    left_forearm = models.FloatField(max_length=100, verbose_name="Левое предплечье", null=True)
    right_forearm = models.FloatField(max_length=100, verbose_name="Правое предплечье", null=True)
    pelvis = models.FloatField(max_length=200, verbose_name="Таз", null=True)
    waist = models.FloatField(max_length=200, verbose_name="Талия", null=True)
    left_thigh = models.FloatField(max_length=100, verbose_name="Бедро левое", null=True)
    right_thigh = models.FloatField(max_length=100, verbose_name="Бедро правое", null=True)
    left_shin = models.FloatField(max_length=100, verbose_name="Голень левая", null=True)
    right_shin = models.FloatField(max_length=100, verbose_name="Голень правая", null=True)
    body_mass_index = models.FloatField(max_length=100, verbose_name="Индекс массы тела", null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", null=True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", null=True)

    @register.filter(name='get_verbose_name_ext')
    def get_verbose_name(self, name):
        return self._meta.get_field(name).verbose_name

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        """
        Calculates the user's BMI
        Formula: weight/height^2
        - weight in kg
        - height in m
        """
        self.body_mass_index = self.weight / self.height**2
        super(UserExtSettings, self).save(*args, **kwargs)

    class Meta:
        ordering = ['user']
        verbose_name = 'Дополнительная настройка'
        verbose_name_plural = 'Дополнительные настройки'
