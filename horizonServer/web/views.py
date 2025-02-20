#from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.urls import reverse
# Create your views here.
def home(request):
  return HttpResponse("hello")
def user(request,userId):
  return HttpResponse("hello 用户Id 为%d" % (userId))
def cater(request):
  id = request.GET.get('id')
  return HttpResponse("你好,id为%s" % (id))
def login(request,paths):
  return HttpResponse(12)
def reflect1(request):
  return HttpResponse("demo111--手动分发路由映射过来的哈哈哈1")
def reflect2(request):
  url = reverse("demo1")
  # reverse("demo1",kwargs={id:"123"}),用于匹配/<str:id>/的路径
  # reverse("demo2",args=(1,2,3)),用于匹配正则表达式的url
  return redirect(url)#这么些就会跳转到demo1对应的路径
  #return HttpResponse("demon2222手动分发路由映射过来的哈哈哈2")