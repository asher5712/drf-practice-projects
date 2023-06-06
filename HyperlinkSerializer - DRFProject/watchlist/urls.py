from django.urls import path
from . import views

urlpatterns = [
    path('list', views.WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', views.WatchListDetailAV.as_view(), name='watch-detail'),
    path('platform', views.StreamPlatformListAV.as_view(), name='streamplatform-list'),
    path('platform/<int:pk>', views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
]