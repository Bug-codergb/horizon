
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request

# Create your views here.
@api_view(['GET'])
def demo(request):
  print(request._request)
  return Response({'app':'v1.0.0'})

class UserView(APIView,):
  def post(self,request,*args,**kwargs):
    print(request.query_params)
    print(request.data)
    print(kwargs)
    return Response("hello")