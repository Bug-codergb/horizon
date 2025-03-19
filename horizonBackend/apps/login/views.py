from django.shortcuts import render
from rest_framework.views import APIView
from utils.response import RetResponse
from apps.user.models import User
from utils.jwt import JsonWebToken

# Create your views here.
class LoginView(APIView):
  authentication_classes = []
  def post(self,request):
    userName = request.data.get("userName")
    password = request.data.get("password")
    user = User.objects.filter(user_name=userName,password=password).first()

    if user is None:
      return RetResponse.info(400,"用户名或者密码错误",None,None,)
    else:
      jwt = JsonWebToken(userId=user.user_id, userName=user.user_name)
      user_json={
        "access_token":jwt.token,
        "userName":user.user_name,
        "userId":user.user_id,
        "description":user.description,
        "gender":user.gender
      }
      jwt.validate(jwt.token+"11")
      return RetResponse.success(user_json,None)