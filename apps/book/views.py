from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializers
from .models import Book

class BookCreateListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers