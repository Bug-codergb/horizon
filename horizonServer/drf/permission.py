from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
  message={"code":403,"message":"权限校验失败"}
  def has_permission(self, request, view):
    return False