from django.http import Http404
from rest_framework import serializers

from author.models import Author
from author.repository import AuthorRepository


class AuthorService:
    def try_to_get_author_or_except(self, author_id) -> Author:
        try:
            author = AuthorRepository().get_by_id(author_id)
        except Http404:
            raise serializers.ValidationError("Not exists author!")

        return author
