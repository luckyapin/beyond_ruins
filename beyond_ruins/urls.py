from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from backend_br.views import *

router_posts = routers.DefaultRouter()
router_posts.register(f'Posts', PostsViewSet, basename='posts')
router_user = routers.DefaultRouter()
router_user.register(f'User', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router_posts.urls)),
    path('api/v1/', include(router_user.urls)),
]
