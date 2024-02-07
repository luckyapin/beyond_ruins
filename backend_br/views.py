from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import *
from .serializer import *
# Create your views here.


class ArticleViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
