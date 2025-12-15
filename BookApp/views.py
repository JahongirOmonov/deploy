from django.shortcuts import render
# Create your views here.\
from .models import BookModel
from rest_framework import generics
from .serializers import BookSerializer


class BookListApiView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

class BookCreateApiView(generics.CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
