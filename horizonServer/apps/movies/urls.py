from django.urls import path
from apps.movies.views import list
urlpatterns = [
    path("list",list),
]
