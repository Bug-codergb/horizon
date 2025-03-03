from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class MyAuthentication(BaseAuthentication):
  def authenticate(self, request):
    token = request.query_params.get("token")
    if token:
      return ("success","1002")
    else :
      raise AuthenticationFailed({"code":401,"message":"请登录"})
  def authenticate_header(self, request):
    return "API"

class HeaderMyAuthentication(BaseAuthentication):
  def authenticate(self, request):
    token = request.META.get("HTTP_AUTHORIZATION")
    if token:
      return ("success","1002")
    else :
      raise AuthenticationFailed({"code":401,"message":"请登录"})