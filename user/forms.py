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





   
class UserRegistrationForm(UserCreationForm):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'input-box',
        'placeholder' : 'Имя'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'input-box',
        'placeholder' : 'Фамилия'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'input-box',
        'placeholder' : 'Username'
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input-box',
        'placeholder': 'Email'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'input-box',
        'placeholder' : 'Введите пароль'
    }))
    
    password2 =  forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'input-box',
        'placeholder' : 'Повторите пароль'
    }))
    
    image =  forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'input-box'
    }))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'image')
        
        
        
        
        
