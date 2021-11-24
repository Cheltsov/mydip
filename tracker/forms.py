from django import forms
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
