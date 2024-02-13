from django.shortcuts import render
from rest_framework import mixins, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import PermissionDenied
from backend_br.models import *
from .serializer import *
from .permissions import *
# Create your views here.


# Обработка всех основных запросов + вывод всех комментариев и категорий у 1 поста
class PostsViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (MyPermission, )

    @action(methods=['get'], detail=True)  # Вывод комментариев к посту
    def comments(self, request, pk):
        coms = Comments.objects.filter(postId=pk)
        j = {}
        for i in coms:
            j[i.pk] = {'commentText': i.commentText,
                       'creationTime': i.creationTime,
                       'userId': i.userId.pk,
                       'postId': int(pk),
                       'username': i.userId.username
                       }
        return Response(j)

    @action(methods=['get'], detail=True)  # Вывод категории поста
    def category(self, request, pk):
        post = Posts.objects.filter(pk=pk)
        return Response({
            'name': post[0].categoryId.name,
        })

# Обработка всех основных запросов к User + вывод всех постов 1 пользователя
class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    @action(methods=['get'], detail=True)  # Вывод всех постов пользователя
    def post(self, request, pk):

        posts = Posts.objects.filter(userId=pk)
        j = {}
        for i in posts:
            j[i.pk] = {'title': i.title,
                       'text': i.text,
                       'creationTime': i.creationTime,
                       'updateTime': i.updateTime,
                       'userId': i.userId.pk,
                       'categoryId': i.categoryId.pk,
                       }
        return Response(j)

    @action(methods=['get'], detail=False)  # Профиль, отправившего токен
    def profile(self, request):
        return Response(request.user.pk)

# Все основные запросы к Категориям
class CategoriesViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (MyPermission,)

# Все основные запросы к комментариям
class CommentsViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (MyPermission,)
