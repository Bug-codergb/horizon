from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
import os
import json

from django.views import View


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
    res = HttpResponse("class view")
    return res
    pass
  def post(self,request):
    pass