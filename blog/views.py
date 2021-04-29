from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Register, Login, CreateComment, Logout, Comment
from .forms import CommentForm


class LoginView(CreateView):
    model = Login
    template_name = 'login.html'
    fields = ['email_address', 'password']


# class RegisterView(CreateView):
#     model = Register
#     template_name = 'register.html'
#     fields = ['username', 'email_address', 'password']


class BlogView(ListView):
    model = Post
    template_name = 'home2.html'


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'



class LogoutOut(ListView):
    model = Logout
    template_name = 'logout.html'
    success_url = reverse_lazy('home')


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home2')


class NewComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'new_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super(NewComment, self).form_valid(form)

    success_url = reverse_lazy('home2')


# use the delete view for the the logout
# use the update view for the reset password
# use the body(where stuff is written for the comment section)
# try adding the details of the new user to a database file
# for the login page, it should read the database file name and
