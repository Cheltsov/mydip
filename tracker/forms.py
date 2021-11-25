from django import forms

from core.models import UserExtSettings
from .models import UserRepository


class MainSettingForm(forms.Form):

    fio = forms.CharField(max_length=100, required=True, label='Фио', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'ФИО'}))
    email = forms.EmailField(max_length=100, required=True, label="Email", widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'Email'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(MainSettingForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserRepository
        fields = ('fio', 'email')

    def clean(self):
        cleaned_data = super(MainSettingForm, self).clean()
        email = cleaned_data.get("email")
        fio = cleaned_data.get("fio")

        if self.user.email != email and UserRepository.getUserByEmail(email):
            print(self.user.email)
            self.add_error('email', "Пользователь уже существует")

        if fio and len(fio) < 10:
            self.add_error('fio', "ФИО должно быть более 10 символов")


class PasswordSettingForm(forms.Form):
    password = forms.CharField(max_length=100, required=True, label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Пароль'}))
    password_repeat = forms.CharField(max_length=100, required=False, label="Пароль", widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': 'Повторите пароль'}))
    password_last = forms.CharField(max_length=100, required=False, label="Пароль", widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': 'Старый пароль'}))

    class Meta:
        model = UserRepository
        fields = 'password'

    def clean(self):
        cleaned_data = super(PasswordSettingForm, self).clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")

        if password and len(password) < 5:
            self.add_error('password', "Пароль должен быть более 5 символов")

        if password and password_repeat and password != password_repeat:
            self.add_error('password_repeat', "Пароли не совпадают")


class SettingsExtForm(forms.ModelForm):
    gender = forms.ChoiceField(required=True, choices=UserExtSettings.CHOICES, label="Пол", widget=forms.Select(attrs={'class': "form-control", 'placeholder': 'Пол'}))
    age = forms.IntegerField(required=True, label='Возраст', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Возраст', 'min': 0}))
    height = forms.DecimalField(required=True, label='Рост', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Рост', 'min': 0}))
    weight = forms.DecimalField(required=True, label='Вес', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Вес', 'min': 0}))
    neck = forms.DecimalField(required=False, label='Обхват шеи', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Обхват шеи', 'min': 0}))
    shoulders = forms.DecimalField(required=False, label='Обхват плечь', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Обхват плечь', 'min': 0}))
    chest_relax = forms.DecimalField(required=False, label='Грудь расслабленная', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Грудь расслабленная', 'min': 0}))
    chest_tense = forms.DecimalField(required=False, label='Грудь напряженная', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Грудь напряженная', 'min': 0}))
    left_biceps_relax = forms.DecimalField(required=False, label='Левый бицепс расслабленный', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Левый бицепс расслабленный', 'min': 0}))
    right_biceps_relax = forms.DecimalField(required=False, label='Правый бицепс расслабленный', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Правый бицепс расслабленный', 'min': 0}))
    left_biceps_tense = forms.DecimalField(required=False, label='Левый бицепс напряженный', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Левый бицепс напряженный', 'min': 0}))
    right_biceps_tense = forms.DecimalField(required=False, label='Правый бицепс напряженный', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Правый бицепс напряженный', 'min': 0}))
    left_forearm = forms.DecimalField(required=False, label='Левое предплечье', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Левое предплечье', 'min': 0}))
    right_forearm = forms.DecimalField(required=False, label='Правое предплечье', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Правое предплечье', 'min': 0}))
    pelvis = forms.DecimalField(required=False, label='Таз', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Таз', 'min': 0}))
    waist = forms.DecimalField(required=False, label='Талия', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Талия', 'min': 0}))
    left_thigh = forms.DecimalField(required=False, label='Бедро левое', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Бедро левое', 'min': 0}))
    right_thigh = forms.DecimalField(required=False, label='Бедро правое', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Бедро правое', 'min': 0}))
    left_shin = forms.DecimalField(required=False, label='Голень левая', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Голень левая', 'min': 0}))
    right_shin = forms.DecimalField(required=False, label='Голень правая', widget=forms.NumberInput(attrs={'class': "form-control", 'placeholder': 'Голень правая', 'min': 0}))

    class Meta:
        model = UserExtSettings
        fields = '__all__'
        exclude = ['user', 'body_mass_index']

    def clean(self):
        cleaned_data = super(SettingsExtForm, self).clean()
        print(cleaned_data)
