import json

from django.http import HttpResponse
from django.shortcuts import render
from user import models
def list(request):
  return HttpResponse("user-list")
def create(request):
  json_data = json.loads(request.body)
  models.Admin.objects.create(**json_data)
  return HttpResponse("创建")
def createDept(request,name):
  models.Department.objects.create(name=name)
  return HttpResponse("创建成功-"+name)
def userDept(request):
  ret = models.Admin.objects.filter(dept__name="市场部")#自动连接表
  print(ret)

  res = models.Admin.objects.filter(id__gt=2).values("id","userId","userName","dept__name")
  print(res)

  e1 = models.Admin.objects.filter(id=2).select_related("dept")
  for item in e1:
    print(item.userName)
  return HttpResponse("用户不萌")