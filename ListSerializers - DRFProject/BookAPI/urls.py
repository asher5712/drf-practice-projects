from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter(trailing_slash=False)
router.register(r'authors', views.AuthorViewSet, basename='author'),
router.register(r'books', views.BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls), name='routes'),
]