from django.contrib.auth import get_user_model

from django.db import models

# БД на ORM
class Categories(models.Model):
    name = models.CharField(max_length=100)
    color = models.TextField()

    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    creationTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    userId = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    categoryId = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    commentText = models.TextField()
    creationTime = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    postId = models.ForeignKey('Posts', on_delete=models.PROTECT)

    def __str__(self):
        return self.commentText


