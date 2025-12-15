from django.urls import path
from .views import BookListApiView, BookCreateApiView

urlpatterns = [
    path('books/', BookListApiView.as_view(), name='books'),
    path('books/create/', BookCreateApiView.as_view(), name='create')
]