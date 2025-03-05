from django.urls import path
from .views.user import CreateUser
urlpatterns=[
  path("create",CreateUser.as_view())
]
app_name = "user"