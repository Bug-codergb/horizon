from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
class AuthMiddleware(MiddlewareMixin):
  def process_request(self,request):
      print("request")
  def process_response(self,request,response):
    print("响应")
    return response