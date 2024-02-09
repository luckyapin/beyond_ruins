from django.shortcuts import render
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import *
from .serializer import *
# Create your views here.


class PostsViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
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
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=True)
    def login(self, request, pk):
        user = User.objects.filter(pk=pk)[0]
        return Response({
            'login': user.userId.username,
            'gender': user.gender,
            'registrationDate': user.registrationDate
        })

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


class CommentsViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Comments.objects.all()
    serializer_class = UserSerializer
