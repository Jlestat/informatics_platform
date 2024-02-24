from django import forms
from .models import Enrollment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course']


class SingUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254,
                             help_text='Обязательное поле. Укажите действующий адрес электронной почты.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
