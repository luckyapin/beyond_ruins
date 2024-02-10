from django.shortcuts import render
from rest_framework import mixins, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import PermissionDenied
from .models import *
from .serializer import *
from .permissions import *
# Create your views here.


class PostsViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (MyPermission, )
    @action(methods=['get'], detail=True)
    def comments(self, request, pk):
        coms = Comments.objects.filter(postId=pk)
        j = {}
        for i in coms:
            j[i.pk] = {'commentText': i.commentText,
                       'creationTime': i.creationTime,
                       'userId': str(i.userId.pk),
                       'postId': pk,
                       'login': i.userId.login
                       }
        return Response(j)

    @action(methods=['get'], detail=True)
    def category(self, request, pk):
        post = Posts.objects.filter(pk=pk)
        return Response({
            'name': post[0].categoryId.name,
            'color': post[0].categoryId.color,
        })


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
    @action(methods=['get'], detail=True)
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


class CategoriesViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Categories.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class CommentsViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Comments.objects.all()
    serializer_class = UserSerializer
    permission_classes = (MyPermission,)
