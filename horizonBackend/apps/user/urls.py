from django.urls import path
from .views.user import CreateUser,AllUserView,DeleteUserView
urlpatterns=[
  path("create",CreateUser.as_view()),
  path("all",AllUserView.as_view()),
  path("delete/<int:user_id>",DeleteUserView.as_view())
]
app_name = "user"