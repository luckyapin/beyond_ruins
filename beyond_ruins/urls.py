from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from backend_br.views import *

router = routers.DefaultRouter()
router.register(f'Posts', PostsViewSet, basename='posts')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
