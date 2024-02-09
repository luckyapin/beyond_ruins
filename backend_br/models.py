from django.db import models


class User(models.Model):
    login = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=25)
    registrationDate = models.DateTimeField(auto_now_add=True)


class Categories(models.Model):
    name = models.CharField(max_length=100)
    color = models.TextField()


class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    creationTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    userId = models.ForeignKey('User', on_delete=models.PROTECT)
    categoryId = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)


class Comments(models.Model):
    commentText = models.TextField()
    creationTime = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey('User', on_delete=models.PROTECT)
    postId = models.ForeignKey('Posts', on_delete=models.PROTECT)


