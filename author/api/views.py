from rest_framework import viewsets
from ..models import Author
from .serializer import AuthorModelSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
