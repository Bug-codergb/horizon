from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from utils.jwt import JsonWebToken

class HeaderTokenAuthentication(BaseAuthentication):
  def authenticate(self, request):
    token = request.META.get("HTTP_AUTHORIZATION")
    print(token)
    print("token")
    if token is not None:
      token = token[7:]
      ret = JsonWebToken().validate(token)
      if ret is None:
        raise AuthenticationFailed({"code":401,"message":"请登录"})
      else:
        request.user_id = ret.get("sub")
        request.user_name = ret.get("name")
    else :
      raise AuthenticationFailed({"code":401,"message":"请登录"})