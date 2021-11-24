from django import forms

from .models import AuthUser


class AuthForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True, label="Email")
    password = forms.CharField(max_length=100, required=True, label="Пароль", widget=forms.PasswordInput())


class SingInForm(forms.Form):
    fio = forms.CharField(max_length=100, required=True, label='Фио', widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'ФИО'}))
    email = forms.EmailField(max_length=100, required=True, label="Email", widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'Email'}))
    password = forms.CharField(max_length=100, required=True, label="Пароль", widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Пароль'}))
    password_repeat = forms.CharField(max_length=100, required=False, label="Пароль", widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = AuthUser
        fields = ('fio', 'email', 'password')

    def clean(self):
        cleaned_data = super(SingInForm, self).clean()
        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")
        email = cleaned_data.get("email")
        fio = cleaned_data.get("fio")

        if password and len(password) < 5:
            self.add_error('password', "Пароль должен быть более 5 символов")

        if password and password_repeat and password != password_repeat:
            self.add_error('password_repeat', "Пароли не совпадают")

        if email and AuthUser.getUserByEmail(email):
            self.add_error('email', "Пользователь уже существует")

        if fio and len(fio) < 10:
            self.add_error('fio', "ФИО должно быть более 10 символов")
