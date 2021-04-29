from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditPasswordFrom


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')


class UserChangePasswordView(generic.UpdateView):
    form_class = EditPasswordFrom
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('home')

    def get_object(self, **kwargs):
        return self.request.user


# class UserUpdateView(generic.UpdateView):
#     form_class = EditPasswordFrom
#     template_name = 'registration/change-password2.html'
#     success_url = reverse_lazy('home')
#
#     def get_object(self):
#         return self.request.user
