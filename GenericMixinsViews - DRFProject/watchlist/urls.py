from django.urls import path
from . import views

urlpatterns = [
    path('list', views.WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', views.WatchListDetailAV.as_view(), name='watch-details'),
    path('platform', views.PlatformListAV.as_view(), name='platform-list'),
    path('platform/<int:pk>', views.PlatformDetailAV.as_view(), name='platform-details'),
    path('platform/<int:pk>/review', views.ReviewList.as_view(), name='review'),
    path('platform/review/<int:pk>', views.ReviewDetail.as_view(), name='review'),
]