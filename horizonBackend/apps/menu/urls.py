from .views.meun import CreateMenuView,AllMenuView,SetRoleMenuView,DeleteMenu,UserRoleMenuListView,RoleMenuView
from django.urls import path
urlpatterns=[
  path("create",CreateMenuView.as_view()),
  path("list",AllMenuView.as_view()),
  path("role",SetRoleMenuView.as_view()),
  path("delete/<int:pk>",DeleteMenu.as_view()),
  path("role/user/<str:id>",UserRoleMenuListView.as_view()),#获取用户菜单
  path("role/<str:id>",RoleMenuView.as_view())
]
app_name="menu"