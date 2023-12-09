from django.urls import path, include
#from watchlist.api.views import movie_list, movie_details
from watchlist.api.views import (WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, StreamPlatformVS, \
                                 ReviewList, ReviewDetail, ReviewCreate, UserReview, WatchListFilter)
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('listfilter/', WatchListFilter.as_view(), name='watchlistfilter'),
    path('', include(router.urls)),
    #path('stream/', StreamPlatformAV.as_view(), name='streamplatform'),
    #path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    #path('review/', ReviewList.as_view(), name='review-list'),
    #path('review/<int:pk>',ReviewDetail.as_view(), name='review-detail')
    path('<int:pk>/reviewcreate/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    #path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),
    path('reviews/', UserReview.as_view(), name='user-review-detail')
]
