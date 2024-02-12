from rest_framework.test import APITestCase, APIRequestFactory
from .views import PostsViewSet
from django.urls import reverse
from rest_framework import status


class PostViewSetTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory
        self.view = PostsViewSet.as_view()
        self.url = reverse('posts')

    def test_view_posts(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)