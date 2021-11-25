# from django.contrib.auth.models import User
from .models import MyUser
from django.core.exceptions import ValidationError
from django.forms import Form
from django import forms
from django.forms.models import ModelForm
import re
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
            MyUser.objects.get(username=inputed_username)
            raise ValidationError("Your username exists")
        except MyUser.DoesNotExist :
            return inputed_username
    
    def clean_email(self):
        inputed_email = self.cleaned_data['email']
        try:
            MyUser.objects.get(email=inputed_email)
            raise ValidationError("Your Email exists")
        except MyUser.DoesNotExist:
            return inputed_email

    def clean_password(self):
        self.password_input = None
        inputed_password = self.cleaned_data['password']
        if not re.findall('[A-Za-z]',  inputed_password) or len(inputed_password) < 8 or not re.findall('[0-9]',  inputed_password):
            raise ValidationError(
                "Your password can't be entirely numeric and must contain at least 8 characters."

                )

        else:
            self.password_input = 'success'
            return inputed_password
    def clean_confirm_password(self):
            if self.password_input == 'success':
                inputed_password = self.cleaned_data['password']
                inputed_confirm_password =self.cleaned_data['confirm_password']
                if inputed_password != inputed_confirm_password:
                    raise ValidationError("password and confirm password do match")
                return inputed_confirm_password
        
    def save_user(self,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        MyUser.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            # sex=self.cleaned_data['sex'],
            email=self.cleaned_data['email'],
            **extra_fields
        )

class EditProfile(forms.ModelForm):
    email = forms.EmailField(required=True, 
        widget=forms.EmailInput(attrs={"class": "edit"})
    )
    first_name = forms.CharField(required=False,
        widget=forms.TextInput(attrs={"class": "edit"})
    )
    last_name = forms.CharField(required=False,
        widget=forms.TextInput(attrs={"class": "edit"})
    )
    dob=forms.CharField(label='Date of Birth',required=False,
        widget=forms.TextInput(attrs={"class": "edit"})
    )
    sex = forms.CharField(required=False,
        widget=forms.TextInput(attrs={"class": "edit"})
    )
    address = forms.CharField(required=False,
        widget=forms.TextInput(attrs={"class": "edit"})
    )
    avatar=forms.CharField(required=False,
        widget=forms.TextInput(attrs={"class": "edit"})
    )
    phone=forms.CharField(required=False,
        widget=forms.TextInput(attrs={"class": "edit"})
    )
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name','dob','sex','address','email','avatar','phone']   