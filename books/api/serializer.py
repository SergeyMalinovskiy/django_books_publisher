from rest_framework import serializers

from books.models import Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField(required=True, max_length=255)
    registration_code = serializers.CharField(required=True, max_length=255)

    # main_author = serializers.IntegerField(source='author.id')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

