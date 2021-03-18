from django.forms import ModelForm
from django.forms import Textarea
from django import forms
from .models import Freeles
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ContactForm(ModelForm):
    class Meta:
        model = Freeles
        fields = ['first_name', 'email', 'message']
        widgets = {
            'message': Textarea(
                attrs = {
                    'placeholder': 'Введите Ваше сообщение'
                }
            )
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']