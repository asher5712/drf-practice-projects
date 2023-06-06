from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('stream', views.StreamPlatformView, basename='streamplatform')

urlpatterns = [
    path('list', views.WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', views.WatchListDetailAV.as_view(), name='watch-details'),
    path('', include(router.urls)),
    # path('platform', views.PlatformListAV.as_view(), name='platform-list'),
    # path('platform/<int:pk>', views.PlatformDetailAV.as_view(), name='platform-details'),
    path('platform/<int:pk>/review', views.ReviewList.as_view(), name='review-list'),
    path('platform/<int:pk>/review-create', views.ReviewCreate.as_view(), name='review-create'),
    path('platform/review/<int:pk>', views.ReviewDetail.as_view(), name='review-details'),
]