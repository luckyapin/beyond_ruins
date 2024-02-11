from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from rest_framework import routers

from backend_br.views import *

router_posts = routers.DefaultRouter()
router_posts.register(f'Posts', PostsViewSet, basename='posts')

router_user = routers.DefaultRouter()
router_user.register(f'User', UserViewSet, basename='user')

router_categories = routers.DefaultRouter()
router_categories.register(f'categories', UserViewSet, basename='categories')

router_comments = routers.DefaultRouter()
router_comments.register(f'comments', UserViewSet, basename='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router_posts.urls)),
    path('api/v1/', include(router_user.urls)),
    path('api/v1/', include(router_categories.urls)),
    path('api/v1/', include(router_comments.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
