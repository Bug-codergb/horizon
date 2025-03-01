from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class MyMd1(MiddlewareMixin):
  def process_request(self,request):
    print("md1请求进入")
  def process_view(self,request,view_func,view_args,views_kwargs):
    print("view")
  def process_response(self,request,response):
    print("md1请求结束")
    return response

class MyMd2(MiddlewareMixin):
  def process_request(self,request):
    print("md2请求进入")
    #return response #HttpResponse("终端")
  def process_response(self,request,response):
    print("md2请求结束")
    return response

class MyMd3(MiddlewareMixin):
  def process_request(self,request):
    print("md3请求进入")
  def process_response(self,request,response):
    print("md3请求结束")
    return response