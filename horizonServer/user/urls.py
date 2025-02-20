from django.urls import path
from user.views import list
urlpatterns = [
    path("list",list),
]
