from django.contrib import admin
from .models import Post, Login, Register, CreateComment, Logout, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Login)
admin.site.register(Register)
admin.site.register(CreateComment)
admin.site.register(Logout)
admin.site.register(Comment)
