from django.contrib.auth import get_user_model
from rest_framework import serializers

from backend_br.models import *

# Сериализаторы, которые преобразуют переменные python в json и обратно
class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
