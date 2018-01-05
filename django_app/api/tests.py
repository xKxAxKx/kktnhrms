import json
import datetime

from django.urls import reverse

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from api.models import About, SNS, Product, Inquiry
from api.views import AboutGetView, SNSGetView, ProductGetView, InquiryPostView


class TestApi(APITestCase):

    def setUp(self):
        # profileの登録(1件目)
        About.objects.get_or_create(name='Yamada',
                                    sub_name='Taro',
                                    real_name='Taro Yamada',
                                    birthday=datetime.datetime(2000, 12, 31),
                                    detail='I am Yamada')

        # profileの登録(1件目)
        About.objects.get_or_create(name='Tanaka',
                                    sub_name='Hanako',
                                    real_name='Hanako Tanaka',
                                    birthday=datetime.datetime(2010, 10, 10),
                                    detail='I am Tanaka')

        # SNSの登録(1件目)
        SNS.objects.get_or_create(name='SNS1',
                                  account_name='SNS1',
                                  url='https://sns1.com',
                                  order=1)

        # SNSの登録(2件目)
        SNS.objects.get_or_create(name='SNS2',
                                  account_name='SNS2',
                                  url='https://sns2.com',
                                  order=3)

        # SNSの登録(3件目)
        SNS.objects.get_or_create(name='SNS3',
                                  account_name='SNS3',
                                  url='https://sns3.com',
                                  order=2)

        # Productの登録(1件目)
        Product.objects.get_or_create(name='product1',
                                      url='https://product1.com',
                                      detail='this is product1',
                                      order=1)

        # Productの登録(2件目)
        Product.objects.get_or_create(name='product2',
                                      url='https://product2.com',
                                      detail='this is product2',
                                      order=3)

        # Productの登録(3件目)
        Product.objects.get_or_create(name='product3',
                                      url='https://product3.com',
                                      detail='this is product3',
                                      order=2)

    def test_get_about(self):
        url = reverse('about')
        response = self.client.get(url)

        self.assertEqual(response.data['name'], 'Yamada')

    def test_list_sns(self):
        url = reverse('sns_list')
        response = self.client.get(url)

        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['name'], 'SNS1')
        self.assertEqual(response.data[1]['name'], 'SNS3')

    def test_retrieve_sns(self):
        url = reverse('sns_get')
        response = self.client.get(url)
        import pdb; pdb.set_trace()

        self.assertEqual(response.data['name'], 'SNS1')
        self.assertEqual(response.data['url'], 'https://sns1.com')

    def test_list_product(self):
        url = reverse('product_list')
        response = self.client.get(url)

        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['name'], 'product2')
        self.assertEqual(response.data[1]['name'], 'product3')

    def test_retrieve_product(self):
        url = reverse('product_get')
        response = self.client.get(url)
        import pdb; pdb.set_trace()

        self.assertEqual(response.data['name'], 'product1')
        self.assertEqual(response.data['url'], 'https://product1.com')

    def test_post_inquiry_success_1(self):
        post_data = {'name': 'name1',
                     'email': 'example@example.com',
                     'message': 'hello!'}
        url = reverse('inquiry')
        response = self.client.post(url, post_data)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 201)

    def test_post_inquiry_success_2(self):
        post_data = {'name': 'test',
                     'email': 'example@example.com',
                     'message': ''}
        url = reverse('inquiry')
        response = self.client.post(url, post_data)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 201)

    def test_post_inquiry_success_3(self):
        post_data = {'name': 'test',
                     'email': 'example@example.com'}
        url = reverse('inquiry')
        response = self.client.post(url, post_data)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 201)

    def test_post_inquiry_error_1(self):
        post_data = {'name': 'name1',
                     'email': 'example.com',
                     'message': 'hello!'}
        url = reverse('inquiry')
        response = self.client.post(url, post_data)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 400)

    def test_post_inquiry_error_2(self):
        post_data = {'name': '',
                     'email': 'example@example.com',
                     'message': 'hello!'}
        url = reverse('inquiry')
        response = self.client.post(url, post_data)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 400)

    def test_post_inquiry_error_3(self):
        post_data = {'name': 'test',
                     'message': 'hello'}
        url = reverse('inquiry')
        response = self.client.post(url, post_data)
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 400)
