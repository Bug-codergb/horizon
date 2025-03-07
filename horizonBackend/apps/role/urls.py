from django.urls import path
from .views.role import CreateRoleView,UserRoleView,AllRoleView,DeleteRoleView
urlpatterns=[
  path("create",CreateRoleView.as_view()),
  path("user",UserRoleView.as_view()),
  path("all",AllRoleView.as_view()),
  path("delete/<int:id>",DeleteRoleView.as_view())
]
app_name="role"