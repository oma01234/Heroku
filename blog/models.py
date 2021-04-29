from django.db import models
from django.urls import reverse


class PostManager(models.Manager):
    def create_post(self, title, body, author):
        post = self.create(title=title, body=body, author=author)
        return post


class Post(models.Model):
    title = models.CharField(max_length=200)
    # to set it to only numbers, use IntField
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    objects = PostManager

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Credentials(models.Manager):
    def create_credential(self, username, email_address, password):
        credentials = self.create_credential(username=username, email_address=email_address, password=password)
        return credentials


class Login(models.Model):
    email_address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('home2')


class Register(models.Model):
    email_address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('home')


class Logout(models.Model):
    logout = models.ForeignKey(Login, related_name='comments', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')


class CreateComment(models.Model):
    post = models.ForeignKey(Post, related_name='commentsnew', on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


