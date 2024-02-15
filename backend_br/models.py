from django.contrib.auth import get_user_model

from django.db import models


# БД на ORM
class Posts(models.Model):
    class Meta:
        app_label = 'backend_br'

    title = models.CharField(max_length=100)
    text = models.TextField()
    creationTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    userId = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    categoryId = models.ForeignKey('Categories', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Categories(models.Model):
    class Meta:
        app_label = 'backend_br'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comments(models.Model):
    class Meta:
        app_label = 'backend_br'

    commentText = models.TextField()
    creationTime = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    postId = models.ForeignKey('Posts', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.commentText


