from django.shortcuts import render
from rest_framework.views import APIView
from utils.response import RetResponse
from utils.jwt import blacklist
# Create your views here.
class LogoutView(APIView):
  authentication_classes = []
  def post(self,request):
    token = request.META.get("HTTP_AUTHORIZATION")
    if token is not None:
      token = token[7:]
      blacklist.add(token)
      return RetResponse.info(403, "您已成功退出当前系统", None, None)
    else :
      return RetResponse.info(403,"当前用户未登录",None, None)