from django import forms
from core.models import UserExtSettings


class CalcCaloriesForm(forms.ModelForm):
    CHOICES = (
        ('1', 'Не определен'),
        ('1.2', 'Сидячий образ жизни'),
        ('1.375', 'Умеренная активность(легкие физические нагрузки либо занятия'),
        ('1.55', 'Средняя активность(занятия 3 - 5 раз в неделю)'),
        ('1.7', 'Высокая активность(интенсивные нагрузки, занятия 6 - 7 раз в неделю)'),
        ('1.9', 'Спортсмены и люди, выполняющие сходные нагрузки(6 - 7раз в неделю)'),
    )

    gender = forms.ChoiceField(required=True, choices=UserExtSettings.CHOICES, label="Пол", widget=forms.Select(attrs={'class': "form-control", 'placeholder': 'Пол'}))
    age = forms.IntegerField(required=True, label='Возраст', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Возраст', 'min': 0}))
    height = forms.DecimalField(required=True, label='Рост', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Рост', 'min': 0}))
    weight = forms.DecimalField(required=True, label='Вес', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Вес', 'min': 0}))
    physic_active = forms.ChoiceField(required=True, choices=CHOICES, label="Степень физической активности", widget=forms.Select(attrs={'class': "form-control", 'placeholder': 'Степень физической активности'}))

    class Meta:
        model = UserExtSettings
        fields = ('age', 'gender', 'height', 'weight')
