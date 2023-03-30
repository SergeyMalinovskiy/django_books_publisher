from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import BookModelSerializer, BookSerializer
from books.models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookListView(APIView):
    def get(self, request: Request, format=None) -> Response:
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)
