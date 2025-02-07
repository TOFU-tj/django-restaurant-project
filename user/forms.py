from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import User
from django import forms

class UserLoginForm(AuthenticationForm): 
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'input-field',
        'placeholder' : "Username"
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'input-field',
        'placeholder' : "Password"
    }))
    
    class Meta: 
        model = User
        fields = ('username', 'password')


        
        