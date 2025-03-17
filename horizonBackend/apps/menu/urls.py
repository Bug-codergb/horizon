from .views.meun import CreateMenuView,AllMenuView,SetRoleMenuView,DeleteMenu,RoleMenuListView
from django.urls import path
urlpatterns=[
  path("create",CreateMenuView.as_view()),
  path("list",AllMenuView.as_view()),
  path("role",SetRoleMenuView.as_view()),
  path("delete/<int:pk>",DeleteMenu.as_view()),
  path("role/<str:id>",RoleMenuListView.as_view()),
]
app_name="menu"