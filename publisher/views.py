from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from publisher.models import Publisher
from publisher.serializers import PublisherModelSerializer


# Create your views here.

class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherModelSerializer
