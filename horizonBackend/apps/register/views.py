from django.shortcuts import render
from rest_framework.views import APIView

from utils.general import generateID
from utils.response import RetResponse
from apps.user.models import User


# Create your views here.
class RegisterView(APIView):
  authentication_classes = []
  def post(self,request):
    data = request.data
    ret = User.objects.filter(user_name=data.get("userName"))
    if len(ret)!=0:
      return RetResponse.info("400","用户已经存在",None,None)
    else:
      id = generateID()
      User.objects.create(user_id=id,
                          user_name=data.get("userName"),
                          gender = 1,
                          password = data.get("password"),
                          description="")
      return RetResponse.success(None,None)