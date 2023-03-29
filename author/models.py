from django.db import models


# Create your models here.
class Author(models.Model):
    surname = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)

    license_code = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)