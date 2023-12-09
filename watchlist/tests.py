from cgitb import reset
from urllib import response
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from watchlist import models
from watchlist.api import serializers


# Create your tests here.
class StreamPlatformTestCase(APITestCase):
    
    def setUp(self):
        self.user=User.objects.create_user(username="TestUser",password="TestPassword@123")
        self.token=Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.stream=models.StreamPlatform.objects.create(name="Test platform",
            about="A Test Platform",
            website="https://www.testplatform.com")
        
    def test_streamplatform_create(self):
        data={
            "name": "Test platform",
            "about": "A Test Platform",
            "website": "https://www.testplatform.com"
        }
        response = self.client.post(reverse('streamplatform-list'), data)
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED) #loi vi normal user khong tao duoc streamplatform
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_streamplatform_index(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class WatchListTestCase(APITestCase):
    def setUp(self):
       self.user=User.objects.create_user(username="TestUser",password="TestPassword@123")
       self.token=Token.objects.get(user__username=self.user)
       self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
       self.stream=models.StreamPlatform.objects.create(name="Test platform",
            about="A Test Platform",
            website="https://www.testplatform.com")
       
       self.watchlist=models.WatchList.objects.create(platform=self.stream,
            title="Test Movie",
            storyline="A test storyline",
            active=True)
       
    def test_watchlist_create(self):
        data={
            "platform": self.stream,
            "title": "Test Movie",
            "storyline": "A test storyline",
            "active": True
        }
        
        response=self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_watchlist_list(self):
        response=self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_watchlist_index(self):
        response=self.client.get(reverse('movie-detail', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.get().title, 'Test Movie')
        self.assertEqual(models.WatchList.objects.count(), 1)
        
class ReviewTestCase(APITestCase):
    def setUp(self):
       self.user=User.objects.create_user(username="TestUser",password="TestPassword@123")
       self.token=Token.objects.get(user__username=self.user)
       self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
       self.stream=models.StreamPlatform.objects.create(name="Test platform",
            about="A Test Platform",
            website="https://www.testplatform.com")
       
       self.watchlist=models.WatchList.objects.create(platform=self.stream,
            title="Test Movie",
            storyline="A test storyline",
            active=True)
       
       self.watchlist2=models.WatchList.objects.create(platform=self.stream,
            title="Test Movie 2",
            storyline="A test storyline 2",
            active=True)
       
       self.review=models.Review.objects.create(review_user=self.user,
            rating=5,
            description="A test review",
            watchlist=self.watchlist2,
            active=True)
            
    def test_review_create(self):
        data={
            "review_user": self.user,
            "rating": 5,
            "description": "A test review",
            "watchlist": self.watchlist,
            "active": True
        }
        
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(models.Review.objects.get().rating, 5)
        self.assertEqual(models.Review.objects.count(), 2)
        
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
    def test_review_create_unauth(self):
        data={
            "review_user": self.user,
            "rating": 5,
            "description": "A test review",
            "watchlist": self.watchlist,
            "active": True
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_review_update(self):
        data={
            "review_user": self.user,
            "rating": 4,
            "description": "A test review updated",
            "watchlist": self.watchlist2,
            "active": False
        }
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Review.objects.get().rating, 4)
        self.assertEqual(models.Review.objects.count(), 1)
        
    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_index(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_review_user(self):
        response = self.client.get('/watch/reviews/?username='+self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)