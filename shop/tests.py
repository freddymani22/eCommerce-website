from django.test import TestCase,Client
from django.contrib.auth import get_user_model

from .models import Checkout,Product


# Create your tests here.


class ProductTestCase(TestCase):

    def setUp(self):
        for i in range(5):
         Product.objects.create(title='tv',price=100,discount=99,category='electronics', description='vintage tv', image ='www.com')
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser', email='testuser@example.com', password='testpass'
        )

    def test_my_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('home')
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], self.user)
    
    def test_queryset_exists(self):
        qs= Product.objects.all()
        self.assertTrue(qs.exists())


    def test_qs_count(self):
       qs = Product.objects.all()
       self.assertEqual(qs.count(), 5)