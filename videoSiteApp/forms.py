from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Укажите логин', label='Логин')
    # email = forms.EmailField(max_length=254, required=True, help_text='Укажите e-mail.')
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=25, required=True, help_text='Пароль должен содержать более 8 букв и/или символов', label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=25, required=True, help_text='Повторите пароль.', label='Повторите пароль')
    widgets = {
        'password1': forms.PasswordInput(),
        'password2': forms.PasswordInput()
    }
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
