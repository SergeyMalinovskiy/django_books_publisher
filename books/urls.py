from django.urls import path

from books.api.views import BookListView

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="list")
]
