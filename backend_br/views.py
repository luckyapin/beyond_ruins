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
    serializer_class = ArticleSerializer
    @action(methods=['get'], detail=True)
    def comments(selfself, request, pk):
        coms = Comments.objects.filter(postId=pk)
        j = {}
        for i in coms:
            j[i.pk] = {'commentText': i.commentText,
                       'creationTime': i.creationTime,
                       'userId': str(i.userId.pk),
                       'postId': pk}
        return Response(j)
