from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
