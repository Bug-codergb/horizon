from django.urls import path
from apps.cinema.views import list
urlpatterns = [
    path("list",list),
]
