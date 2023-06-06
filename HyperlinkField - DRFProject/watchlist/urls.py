from django.urls import path
from . import views

urlpatterns = [
    path('list', views.WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', views.WatchListDetailAV.as_view(), name='watch-details'),
    path('platform', views.PlatformListAV.as_view(), name='platform-list'),
    path('platform/<int:pk>', views.PlatformDetailAV.as_view(), name='platform-details'),
]