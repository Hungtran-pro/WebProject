from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import Form
from django import forms

class Register(Form):
    username = forms.CharField(
        label="UserName",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id': 'username'
            }
        )
    )
    password = forms.CharField(
        label="PassWord",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id': 'password'
            }
        )
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id': 'confirm_password'
            }
        )
    )
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id': 'first_name'
            }
        )
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id': 'last_name'
            }
        )
    )
    email = forms.CharField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'id': 'email'
            }
        )
    )
    def clean_username(self):
        inputed_username = self.cleaned_data['username']
        try:
            User.objects.get(username=inputed_username)
            raise ValidationError("Your username exists")
        except User.DoesNotExist :
            return inputed_username
    
    def clean_email(self):
        inputed_email = self.cleaned_data['email']
        try:
            User.objects.get(email=inputed_email)
            raise ValidationError("Your Email exists")
        except User.DoesNotExist:
            return inputed_email
    def clean_confirm_password(self):
        inputed_password = self.cleaned_data['password']
        inputed_confirm_password =self.cleaned_data['confirm_password']   
        if inputed_password != inputed_confirm_password:
            raise ValidationError("password and confirm password do match")
        return inputed_confirm_password
    def save_user(self,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            **extra_fields

        )