from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.views import APIView
from rest_framework.request import Request
from drf.permission import MyPermission


# Create your views here.
@api_view(['GET'])
def demo(request):
  print(request._request)
  return Response({'app':'v1.0.0'})

class UserView(APIView):
  # authentication_classes = [MyAuthentication]可以全局应用 优先
  permission_classes = [MyPermission]
  def post(self,request,*args,**kwargs):
    print(request.query_params)
    print(request.data)
    print(kwargs)

    print(request.user)
    print(request.auth)
    return Response("hello")
