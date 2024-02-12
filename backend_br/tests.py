from rest_framework.test import APITestCase, APIRequestFactory
from .views import PostsViewSet
from django.urls import reverse
from rest_framework import status
from beyond_ruins_project import urls


class PostViewSetTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('posts-list')

    def test_view_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)