from django.urls import path
from .views import UserRegisterView, UserChangePasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('change-password2/', UserChangePasswordView.as_view(), name='change-password2'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password2.html')),
]
