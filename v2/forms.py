from django import forms
from .models import User

class RegisterForm(forms.Form):

    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':"form-control"}))
    last_name= forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':"form-control"}))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':"form-control"}))
    confirm_password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':"form-control"}))
    address = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':"form-control"}))

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': "form-control"}))


class ComplaintForm(forms.Form):
    fullname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}),label='Full Name')
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}),label='Email Address')
    comment = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class':"form-control"}), label='Comment')

    '''first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=90)
    address = models.CharField(max_length=500)'''