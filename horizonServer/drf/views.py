import os
from django.conf import settings
from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.views import APIView
from rest_framework import serializers
from drf.permission import MyPermission
from setting import models

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


class UserInfoSerializer(serializers.Serializer):
  name = serializers.CharField()
  age = serializers.IntegerField()
  description = serializers.CharField()
  gender = serializers.CharField()

class UserInfoView(APIView):
  def post(self,request):
    user_object = models.User.objects.all()#.first()
    print(user_object)
    ser = UserInfoSerializer(instance=user_object,many=True)
    return Response(ser.data)



class AllUserInfoSerializer(serializers.ModelSerializer):
  gender_text = serializers.CharField(source="get_gender_display")
  address_text = serializers.CharField(source="address")

  xx = serializers.SerializerMethodField()
  class Meta:
    model = models.User
    #fields = "__all__" 全部字段
    fields = ["name","age","gender","description","gender_text","address_text","xx"]
  def get_xx(self,obj):
    return "{}-{}-{}".format(obj.name,obj.age,obj.gender)

class AllUserInfoView(APIView):
  def post(self,request):
    user_object = models.User.objects.all()  # .first()
    ser = AllUserInfoSerializer(instance=user_object, many=True)
    ctx = {
      "code":200,
      "data":ser.data
    }
    return Response(ctx)