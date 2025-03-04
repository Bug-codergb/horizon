import os
from django.conf import settings
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

class ParamsView(APIView):
  def post(self,request):
    #print(request.data)
    #print(request.data['app'])
    file_object = request.data.get('file')
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')

    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file_object.name)
    # 保存文件到本地
    with open(file_path, 'wb+') as destination:
      for chunk in file_object.chunks():
        destination.write(chunk)

    return Response("success")
