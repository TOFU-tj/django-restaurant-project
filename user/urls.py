from django.urls import path
from user.views import UserRegistrationView, UserLoginView, EmailVerificationView
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path("verify/<str:email>/<uuid:code>/", EmailVerificationView.as_view(), name="email_verification")

]
