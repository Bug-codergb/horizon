from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.shortcuts import redirect, render
from django.urls import reverse
import os
import json

from django.views import View
from setting import models

# Create your views here.
def list(request):
  urls = reverse("x1:u")#别人的
  print(urls)

  #print(request.path_info)
  #print(request.GET)
  #print(request.method)
  #print(request.body)
  #print(request.resolver_match)

  #print(request.POST)
  #print(request.FILES.get("avatar"))
  #print(request.headers)

  #json_data = json.loads(request.body)
  #print(json_data['name'])
  #return redirect("https://bilibili.com") #可以url的name
  #return HttpResponse("setting",content_type="application/json")
  #return render(request,"login.html") # 默认在setting.py/TEMPLATES.DIRS里面去找

  res = HttpResponse("hello")
  res['content-type']="application/json"
  res.set_cookie("sessonid","guobinlina")
  return res
class DeleteView(View):
  def get(self,request):

    models.User.objects.create(name="张三",age=24,description="一家")
    models.User.objects.create(**{"name":"姥爷","age":54,"description":"星河好啊"})

    obj = models.User(name="赵洁",age=34,description="漂亮",address="集宁")
    obj.save()
    res = HttpResponse("class view")
    return res
    pass
  def post(self,request):
    pass
def rawDel(request,id):
  print(id)
  #models.User.objects.all().delete()
  ret = models.User.objects.filter(id=id).delete()
  print(ret)
  return HttpResponse("liha")
def update(request,id,name):
  # models.User.objects.filter(id=id).update(**{"name":2323,"age":333})
  models.User.objects.filter(id=id).update(name=name,age=12)
  return HttpResponse("更新")
def all(request):
  ret = models.User.objects.all()

  e1 = models.User.objects.filter(age__gt=2)#大于2
  print(e1.query)
  e2 = models.User.objects.filter(age__gte=3)#大于等于3
  print(e2.query)
  e3 = models.User.objects.filter(id__lt = 2)#小雨2
  print(e3.query)
  e4 = models.User.objects.filter(id__in=[1,2,3])
  print(e4.query)
  e5 = models.User.objects.filter(name__contains="we")
  print(e5.query)
  # models.User.objects.exclude(id=4) 过滤出id不等于4
  # models.User.objects.filter(id__startswith=4)
  l = []
  for item in ret:

    m = {
      "id":item.id,
      "name":item.name,
      "age":item.age,
      "description":item.description,
      "address":item.address,
      "gender":item.gender
    }
    l.append(m)
  return HttpResponse(json.dumps(l),content_type="application/json")#JsonResponse(ret)