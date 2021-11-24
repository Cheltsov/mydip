from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from core.models import User


# Create your models here.
class UserExtSettings(models.Model):
    MAN = 'man'
    WOMAN = 'woman'
    CHOICES = (
        (MAN, 'Man'),
        (WOMAN, 'Woman'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=5, choices=CHOICES, default='MAN')
    age = models.IntegerField(verbose_name="Возраст", blank=True, default=1,
                              validators=[
                                  MaxValueValidator(120),
                                  MinValueValidator(1)
                              ])
    height = models.FloatField(max_length=300, verbose_name="Рост", blank=True)
    weight = models.FloatField(max_length=200, verbose_name="Вес", blank=True)
    neck = models.FloatField(max_length=100, verbose_name="Шея", blank=True)
    shoulders = models.FloatField(max_length=200, verbose_name="Плечи", blank=True)
    chest_relax = models.FloatField(max_length=200, verbose_name="Грудь расслабленная", blank=True)
    chest_tense = models.FloatField(max_length=200, verbose_name="Грудь напряженная", blank=True)
    left_biceps_relax = models.FloatField(max_length=100, verbose_name="Левый бицепс расслабленный", blank=True)
    right_biceps_relax = models.FloatField(max_length=100, verbose_name="Правый бицепс расслабленный", blank=True)
    left_biceps_tense = models.FloatField(max_length=100, verbose_name="Левый бицепс напряженный", blank=True)
    right_biceps_tense = models.FloatField(max_length=100, verbose_name="Правый бицепс напряженный", blank=True)
    left_forearm = models.FloatField(max_length=100, verbose_name="Левое предплечье", blank=True)
    right_forearm = models.FloatField(max_length=100, verbose_name="Правое предплечье", blank=True)
    pelvis = models.FloatField(max_length=200, verbose_name="Таз", blank=True)
    waist = models.FloatField(max_length=200, verbose_name="Талия", blank=True)
    left_thigh = models.FloatField(max_length=100, verbose_name="Бедро левое", blank=True)
    right_thigh = models.FloatField(max_length=100, verbose_name="Бедро правое", blank=True)
    left_shin = models.FloatField(max_length=100, verbose_name="Голень левая", blank=True)
    right_shin = models.FloatField(max_length=100, verbose_name="Голень правая", blank=True)
    body_mass_index = models.FloatField(max_length=100, verbose_name="Индекс массы тела", blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", blank=True)
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", blank=True)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        """
        Calculates the user's BMI
        Formula: weight/height^2
        - weight in kg
        - height in m
        """
        self.body_mass_index = self.weight / pow(self.height, 2)
        super(UserExtSettings, self).save(*args, **kwargs)

    class Meta:
        ordering = ['user']
        verbose_name = 'Дополнительная настройка'
        verbose_name_plural = 'Дополнительные настройки'
