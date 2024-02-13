from rest_framework.test import APITestCase, APIRequestFactory
from .views import PostsViewSet
from django.urls import reverse
from rest_framework import status
from beyond_ruins_project import urls
from django.contrib.auth import get_user_model
import json

user = get_user_model()


class PostViewSetTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('posts-list')

    def authenticate(self):
        data = {
            'username': "testuser",
            'password': "testpassword",
            'email': "testemail@mail.com"
        }
        data2 = {
            'username': "testuser",
            'password': "testpassword",
        }

        self.client.post('/api/v1/auth/users/', data=json.dumps(data), content_type='application/json')
        response = self.client.post(reverse('token_obtain_pair'), data=json.dumps(data2),
                                    content_type='application/json')
        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_view_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_creation(self):
        sample_post = {
            'title': "testpost",
            'text': 'asd',
            'userId': '1'
        }
        self.authenticate()
        response = self.client.post(reverse('posts-list'), json.dumps(sample_post), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)
        self.assertEqual(response.data['title'], 'testpost')

    def test_post_deletion(self):
        self.authenticate()
        post_id = 1
        delete_url = f"/api/v1/Posts/{post_id}/"
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # 'posts-detail', kwargs={'pk': post_id}