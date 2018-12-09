from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .models import Product, Profile
from .models import Newusers, Nuser, tinytest

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = Nuser
        fields = [
            'name',
            'phone',
            'address',
            'occupation',
            'email',
            'password',
            'image'
        ]

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

        #validating password
        def clean_password(self):
            cd = self.cleaned_data
            if cd['password2'] != cd['password']:
                raise ValidationError("Password Don't match")

            return cd['password']


class Userform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'pattern': '[A-Za-z ]+', 'placeholder':'Enter Username', }), required=True, max_length=50, )
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email ID'}), required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','pattern': '[A-Za-z ]+', 'placeholder':'Enter first name'}), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','pattern': '[A-Za-z ]+', 'placeholder':'Enter last name'}), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter password'}), required=True, max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm password again'}), required=True, max_length=50)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username', }), required=False,max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}), required=False,max_length=50)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # user_qs = User.objects.filter(username=username, password=password)
        # if user_qs.count()==1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class tinyFormTest(forms.ModelForm):
	class Meta:
		model = tinytest
		fields = ('name','email')

class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'photo', 'attachment',)