from django.shortcuts import render
from rest_framework.views import APIView
from utils.response import RetResponse

# Create your views here.
class LoginView(APIView):
  def post(self,request):
    user={
      "access_token":"123",
      "userName":"叶子",
      "userId":"1741261813698"
    }
    return RetResponse.success(user,None)