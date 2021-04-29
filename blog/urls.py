from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView\
    , BlogView, NewComment
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/post_new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/new_comment/', NewComment.as_view(), name='new_comment'),
    path('post/', BlogView.as_view(), name='home2'),
    # .as_view is a class base view
]
