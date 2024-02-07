from django.db import models


class User(models.Model):
    login = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=25)
    registration_date = models.DateTimeField(auto_now_add=True)


class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=100)
    main_text = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)
    category_id = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)


class Comments(models.Model):
    comment_text = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)
    article_id = models.ForeignKey('Article', on_delete=models.PROTECT)


