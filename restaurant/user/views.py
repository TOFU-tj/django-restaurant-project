from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, HttpResponseRedirect
from user.models import User, EmailVerification
from user.forms import UserLoginForm, UserRegistrationForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from main.models import Basket


from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView


class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    form_class = UserLoginForm
    

    
    

class BasketUpdateView(UpdateView):
    model = Basket
    template_name = "main/order_page.html"
    
    def get_success_url(self): 
        return reverse_lazy('main:order_page', args = (self.object.id))
        
    



def logout(request): 
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
    


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    template_name = "user/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user:login')

    success_message = 'На указанный вами email было отправлено письмо для подтверждения. Пожалуйста, перейдите по ссылке в письме, чтобы завершить процесс верификации.'
    
    


class EmailVerificationView(TemplateView): 
    template_name = 'user/email_verification.html'
    
    def get(self, request, *args, **kwargs): 
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() : 
            verification = email_verifications.first()
            if not verification.is_expired():
                
                user.is_verified_email = True
                user.save()
                return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else : 
            return HttpResponseRedirect(reverse('index'))




            


    
